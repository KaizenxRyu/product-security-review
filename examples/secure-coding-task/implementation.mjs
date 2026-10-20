function fail(status, message) {
  const error = new Error(message);
  error.status = status;
  throw error;
}

function validId(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

function principal(ctx) {
  const user = ctx?.user;
  if (!user || !validId(user.id) || !validId(user.tenantId) ||
      !Array.isArray(user.permissions) ||
      !user.permissions.every(permission => typeof permission === 'string')) {
    fail(401, 'Authentication required');
  }
  return user;
}

function request(input) {
  if (!input || typeof input !== 'object' || Array.isArray(input)) {
    fail(400, 'Invalid input');
  }
  return input;
}

function invoiceFor(user, invoiceId, store) {
  if (!validId(invoiceId)) fail(400, 'Invalid invoiceId');
  const invoice = store.invoices.find(item =>
    item.id === invoiceId && item.tenantId === user.tenantId
  );
  if (!invoice) fail(404, 'Invoice not found');
  return invoice;
}

export function health() {
  return { status: 'ok' };
}

export function getInvoice(ctx, input, store) {
  const user = principal(ctx);
  const invoice = invoiceFor(user, request(input).invoiceId, store);
  return {
    id: invoice.id,
    tenantId: invoice.tenantId,
    paidCents: invoice.paidCents,
    refundedCents: invoice.refundedCents,
    currency: invoice.currency
  };
}

export function searchDocs(ctx, input, store) {
  const user = principal(ctx);
  const { query } = request(input);
  if (typeof query !== 'string' || query.trim().length === 0 || query.length > 500) {
    fail(400, 'Query must be a nonempty string of at most 500 characters');
  }
  const needle = query.toLowerCase();
  return store.documents
    .filter(document => document.tenantId === user.tenantId)
    .filter(document => document.text.toLowerCase().includes(needle))
    .map(document => ({
      id: document.id,
      tenantId: document.tenantId,
      text: document.text
    }));
}

export function prepareRefund(ctx, input, store) {
  const user = principal(ctx);
  if (!user.permissions.includes('refund:prepare')) {
    fail(403, 'Refund preparation is not permitted');
  }
  const { invoiceId, amountCents, approvalId } = request(input);
  const invoice = invoiceFor(user, invoiceId, store);
  if (!Number.isSafeInteger(amountCents) || amountCents <= 0) {
    fail(400, 'Invalid amountCents');
  }
  if (!validId(approvalId)) fail(400, 'Invalid approvalId');
  if (!Number.isSafeInteger(invoice.paidCents) || invoice.paidCents < 0 ||
      !Number.isSafeInteger(invoice.refundedCents) || invoice.refundedCents < 0 ||
      invoice.refundedCents > invoice.paidCents) {
    fail(400, 'Invalid invoice balance');
  }
  const remainingCents = invoice.paidCents - invoice.refundedCents;
  if (amountCents > remainingCents) fail(400, 'Amount exceeds remaining balance');
  const approval = store.approvals.find(record =>
    record.id === approvalId &&
    record.state === 'approved' &&
    record.tenantId === user.tenantId &&
    record.actorId === user.id &&
    record.invoiceId === invoice.id &&
    record.amountCents === amountCents
  );
  if (!approval) fail(403, 'Matching approval required');
  return {
    status: 'prepared',
    invoiceId: invoice.id,
    tenantId: user.tenantId,
    actorId: user.id,
    amountCents,
    currency: invoice.currency,
    approvalId: approval.id
  };
}
