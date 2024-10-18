# -*- coding: utf-8 -*-

from odoo import api, fields, models, Command, _, osv

class AccountChartTemplate(models.Model):
    _inherit= "account.chart.template"

    def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):
        journal_data = super()._prepare_all_journals(acc_template_ref, company, journals_dict=journals_dict)
        for journal in journal_data:
            if journal['code'] == '杂项':
                journal.update({'name': '手工录入', 'code': '记'})
        return journal_data
