# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command, _, osv

class AccountChartTemplate(models.Model):
    _inherit= "account.chart.template"

    @api.model
    def generate_journals(self, acc_template_ref, company, journals_dict=None):
        journal_data = super(AccountChartTemplate, self).generate_journals(acc_template_ref, company, journals_dict=journals_dict)
        for journal in journal_data:
            if journal['code'] == _('MISC'):
                journal['name'] = '手工录入'
                journal['code'] = '记'
                break

        return journal_data
