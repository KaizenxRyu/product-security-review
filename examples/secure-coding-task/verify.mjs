// Run only against a reviewed synthetic implementation, never against an unknown downloaded module.
import {test} from 'node:test';
import assert from 'node:assert/strict';
import {health,getInvoice,searchDocs,prepareRefund} from './implementation.mjs';

const principal=()=>({user:{id:'user-a',tenantId:'tenant-a',permissions:['refund:prepare']}});
const data=()=>({
 invoices:[{id:'INV-A',tenantId:'tenant-a',paidCents:1000,refundedCents:200,currency:'INR',internalNote:'synthetic-internal-only'},{id:'INV-B',tenantId:'tenant-b',paidCents:10000,refundedCents:0,currency:'INR',internalNote:'B-private'}],
 documents:[{id:'DOC-A',tenantId:'tenant-a',text:'Policy for refunds'},{id:'DOC-B',tenantId:'tenant-b',text:'Policy for refunds'}],
 approvals:[{id:'approval-1',state:'approved',tenantId:'tenant-a',actorId:'user-a',invoiceId:'INV-A',amountCents:800}]
});
const request=()=>({invoiceId:'INV-A',amountCents:800,approvalId:'approval-1'});
async function rejectsStatus(fn,status){await assert.rejects(async()=>await fn(),e=>e.status===status);}

test('health is public',async()=>assert.deepEqual(await health(),{status:'ok'}));
test('own invoice and data minimization',async()=>{const out=await getInvoice(principal(),{invoiceId:'INV-A'},data());assert.equal(out.id,'INV-A');assert.equal('internalNote' in out,false);});
test('protected read denies missing identity',()=>rejectsStatus(()=>getInvoice({}, {invoiceId:'INV-A'},data()),401));
test('foreign invoice cannot be selected',()=>rejectsStatus(()=>getInvoice(principal(),{invoiceId:'INV-B',tenantId:'tenant-b'},data()),404));
test('document search binds trusted tenant',async()=>{const out=await searchDocs(principal(),{query:'policy',tenantId:'tenant-b',role:'admin'},data());assert.deepEqual(out.map(d=>d.id),['DOC-A']);});
test('search rejects empty query',()=>rejectsStatus(()=>searchDocs(principal(),{query:''},data()),400));
test('search rejects oversized query',()=>rejectsStatus(()=>searchDocs(principal(),{query:'a'.repeat(501)},data()),400));
test('search requires identity',()=>rejectsStatus(()=>searchDocs({}, {query:'policy'},data()),401));
test('valid refund prepares exact intent without mutation',async()=>{const store=data();const before=structuredClone(store);assert.deepEqual(await prepareRefund(principal(),request(),store),{status:'prepared',invoiceId:'INV-A',tenantId:'tenant-a',actorId:'user-a',amountCents:800,currency:'INR',approvalId:'approval-1'});assert.deepEqual(store,before);});
test('refund requires identity',()=>rejectsStatus(()=>prepareRefund({},request(),data()),401));
test('refund requires server permission, not body role',()=>{const ctx=principal();ctx.user.permissions=[];return rejectsStatus(()=>prepareRefund(ctx,{...request(),role:'admin',approved:true},data()),403);});
test('foreign invoice refund denied',()=>rejectsStatus(()=>prepareRefund(principal(),{...request(),invoiceId:'INV-B'},data()),404));
test('caller approval flag is not server approval',()=>rejectsStatus(()=>prepareRefund(principal(),{...request(),approvalId:'missing',approved:true},data()),403));
for(const field of ['tenantId','actorId','invoiceId','amountCents','state'])test('approval must bind '+field,()=>{const store=data();store.approvals[0][field]=field==='amountCents'?1:'different';return rejectsStatus(()=>prepareRefund(principal(),request(),store),403);});
for(const amount of [-1,0,0.5,'800',Number.MAX_SAFE_INTEGER+1,801])test('invalid or excessive amount '+amount,()=>rejectsStatus(()=>prepareRefund(principal(),{...request(),amountCents:amount},data()),400));
