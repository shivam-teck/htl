from odoo import api, fields, models,_
from datetime import date, timedelta
from odoo.tools import format_amount
from odoo.exceptions import UserError, ValidationError


class AccountPayment(models.Model):
    _inherit = "account.payment"

    order_id = fields.Many2one('sale.order', string="Order")
    term_id = fields.Many2one('payments.by.term')

    @api.ondelete(at_uninstall=False)
    def restrict_delete(self):
        if self.state == 'posted':
            raise ValidationError("You can delete payment one's the payment is done.")