# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command, _, osv

class AccountChartTemplate(models.Model):
    _inherit= "account.chart.template"

    @api.model
    def generate_journals(self, acc_template_ref, company, journals_dict=None):
        result = super(AccountChartTemplate, self).generate_journals(acc_template_ref, company, journals_dict=journals_dict)
        journal = self.env['account.journal'].search([('code', '=', _('MISC'))])
        journal.write({'name': '手工录入', 'code': '记'})

        return result
