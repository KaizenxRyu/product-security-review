// Inert review fixture. Deliberately incomplete; do not deploy this file.
import { app, db, requireSession, retrieve, sendRefund } from './provided';

app.get('/health', (_req, res) => res.json({ status: 'ok' })); // Intentional public endpoint.
app.use('/api', requireSession); // All /api handlers below require a valid session.

app.get('/api/invoices/:id', async (req, res) => {
  const invoice = await db.invoice.findUnique({ where: { id: req.params.id } });
  res.json(invoice);
});

app.get('/api/scoped-invoices/:id', async (req, res) => {
  const invoice = await db.invoice.findFirst({
    where: { id: req.params.id, tenantId: req.user.tenantId },
  });
  if (!invoice) return res.status(404).end();
  res.json(invoice);
});

app.post('/api/assistant/search', async (req, res) => {
  const matches = await retrieve(req.body.query, { tenantId: req.body.tenantId });
  res.json(matches);
});

app.post('/api/assistant/refund', async (req, res) => {
  if (req.body.approved !== true) return res.status(403).end();
  res.json(await sendRefund(req.body.invoiceId, req.body.amount));
});
