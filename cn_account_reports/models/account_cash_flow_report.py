# -*- coding: utf-8 -*-
from odoo import models


class CashFlowReportCustomHandler(models.AbstractModel):
    _inherit = 'account.cash.flow.report.handler'

    def _custom_options_initializer(self, report, options, previous_options=None):
        super()._custom_options_initializer(report, options, previous_options=previous_options)
        # 取消日记账限制
        report._init_options_journals(options, previous_options=previous_options)
