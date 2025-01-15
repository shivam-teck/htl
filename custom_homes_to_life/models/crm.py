from odoo import models, api, fields, _


class InheritCrmLead(models.Model):
    _inherit = "crm.lead"

    # type = fields.Selection([
    #     ('lead', 'Lead'), ('opportunity', 'Opportunity')], required=True, tracking=15, index=True,
    #     default=lambda self: 'lead' if self.env['res.users'].has_group('crm.group_use_lead') else 'opportunity')

    memo = fields.Text('Memo')
    sale_staff = fields.Many2one('hr.employee')
    is_ho_account = fields.Boolean('HO account', default=False, compute='compute_ho_account')

    @api.depends('company_id','partner_id')
    def compute_ho_account(self):
        for rec in self:
            if rec.company_id.business_type == 'ho':
                rec.is_ho_account = True
            else:
                rec.is_ho_account = False

    @api.model
    def create(self, vals):
        company_id = vals.get('company_id')
        print(company_id,'company_is')





        # Call the original create method to create the product
        return super(InheritCrmLead, self).create(vals)



    # def convert_to_lead(self):
    #     if self.type == 'opportunity':
    #         self.type = 'lead'
    #     else:
    #         pass
