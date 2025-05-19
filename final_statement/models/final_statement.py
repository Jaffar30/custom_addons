from odoo import models, fields, api
from odoo.exceptions import ValidationError

class FinalStatement(models.Model):
    _name = 'final.statement'

    name = fields.Char(string='Name', required=True)
    purchase_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)
    vendor_id = fields.Many2one('res.partner', string='Vendor', related='purchase_id.partner_id', store=True)
    bill_ids = fields.Many2many(
        'account.move',
        related='purchase_id.invoice_ids',
        string='Bills',
    )
    bill_count = fields.Integer(string='Bill Count', compute='_compute_bill_count', store=True)
    total_amount = fields.Monetary(
        string='Total Amount',
        currency_field='currency_id',
        compute='_compute_total_amount',
        store=True
    )
    currency_id = fields.Many2one('res.currency', string='Currency', related='purchase_id.currency_id', store=True)


    def _compute_bill_count(self):
        for record in self:
            record.bill_count = len(record.bill_ids)

    @api.depends('bill_ids.amount_total')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(record.bill_ids.mapped('amount_total'))

    def print_final_statement(self):
        self.ensure_one()
        return self.env.ref('final_statement.final_statement_report_action').report_action(self)