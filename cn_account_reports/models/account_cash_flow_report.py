# -*- coding: utf-8 -*-
from odoo import models


class CashFlowReportCustomHandler(models.AbstractModel):
    _name = 'cn_account.cash.flow.report.handler'
    _inherit = 'account.cash.flow.report.handler'

    def _dispatch_aml_data(self, tags_ids, aml_data, layout_data, report_data):
        # Dispatch the aml_data in the correct layout_line
        if aml_data['account_account_type'] == 'asset_receivable':
            self._add_report_data('advance_payments_customer', aml_data, layout_data, report_data)
        elif aml_data['account_account_type'] == 'liability_payable':
            self._add_report_data('advance_payments_suppliers', aml_data, layout_data, report_data)
        elif aml_data['balance'] < 0:
            if aml_data['account_tag_id'] == tags_ids['operating']:
                self._add_report_data('paid_operating_activities', aml_data, layout_data, report_data)
            elif aml_data['account_tag_id'] == tags_ids['investing']:
                self._add_report_data('investing_activities_cash_out', aml_data, layout_data, report_data)
            elif aml_data['account_tag_id'] == tags_ids['financing']:
                self._add_report_data('financing_activities_cash_out', aml_data, layout_data, report_data)
            else:
                self._add_report_data('unclassified_activities_cash_out', aml_data, layout_data, report_data)
        elif aml_data['balance'] > 0:
            if aml_data['account_tag_id'] == tags_ids['operating']:
                self._add_report_data('received_operating_activities', aml_data, layout_data, report_data)
            elif aml_data['account_tag_id'] == tags_ids['investing']:
                self._add_report_data('investing_activities_cash_in', aml_data, layout_data, report_data)
            elif aml_data['account_tag_id'] == tags_ids['financing']:
                self._add_report_data('financing_activities_cash_in', aml_data, layout_data, report_data)
            else:
                self._add_report_data('unclassified_activities_cash_in', aml_data, layout_data, report_data)

    # -------------------------------------------------------------------------
    # COLUMNS / LINES
    # -------------------------------------------------------------------------
    def _get_layout_data(self):
        # Indentation of the following dict reflects the structure of the report.
        return {
            'operating_activities': {'name': '一、经营活动产生的现金流量：', 'level': 0},
                'advance_payments_customer': {'name': '销售商品、提供劳务收到的现金', 'level': 1, 'parent_line_id': 'operating_activities'},
                'tax_in': {'name': '收到的税费返还', 'level': 1, 'parent_line_id': 'operating_activities'},
                'received_operating_activities': {'name': '收到其他与经营活动有关的现金', 'level': 1, 'parent_line_id': 'operating_activities'},
                'operating_in': {'name': '　经营活动现金流入小计', 'level': 1, 'parent_line_id': 'operating_activities'},
                'advance_payments_suppliers': {'name': '购买商品、接受劳务支付的现金', 'level': 1, 'parent_line_id': 'operating_activities'},
                'employee': {'name': '支付给职工以及为职工支付的现金', 'level': 1, 'parent_line_id': 'operating_activities'},
                'tax_out': {'name': '支付的各项税费', 'level': 1, 'parent_line_id': 'operating_activities'},
                'paid_operating_activities': {'name': '支付其他与经营活动有关的现金', 'level': 1, 'parent_line_id': 'operating_activities'},
                'operating_out': {'name': '　经营活动现金流出小计', 'level': 1, 'parent_line_id': 'operating_activities'},
                'operating_net': {'name': '　　经营活动产生的现金流量净额', 'level': 1, 'parent_line_id': 'operating_activities'},
            'investing_activities': {'name': '二、投资活动产生的现金流量：', 'level': 0},
                'invest_in': {'name': '收回投资收到的现金', 'level': 1, 'parent_line_id': 'investing_activities'},
                'invest_income': {'name': '取得投资收益收到的现金', 'level': 1, 'parent_line_id': 'investing_activities'},
                'asset_in': {'name': '处置固定资产、无形资产和其他长期资产收回的现金净额', 'level': 1, 'parent_line_id': 'investing_activities'},
                'subsidiary_in': {'name': '处置子公司及其他营业单位收到的现金净额', 'level': 1, 'parent_line_id': 'investing_activities'},
                'investing_activities_cash_in': {'name': '收到其他与投资活动有关的现金', 'level': 1, 'parent_line_id': 'investing_activities'},
                'investing_in': {'name': '　投资活动现金流入小计', 'level': 1, 'parent_line_id': 'investing_activities'},
                'asset_out': {'name': '购建固定资产、无形资产和其他长期资产支付的现金', 'level': 1, 'parent_line_id': 'investing_activities'},
                'invest_out': {'name': '投资支付的现金', 'level': 1, 'parent_line_id': 'investing_activities'},
                'subsidiary_out': {'name': '取得子公司及其他营业单位支付的现金净额', 'level': 1, 'parent_line_id': 'investing_activities'},
                'investing_activities_cash_out': {'name': '支付其他与投资活动有关的现金', 'level': 1, 'parent_line_id': 'investing_activities'},
                'investing_out': {'name': '　投资活动现金流出小计', 'level': 1, 'parent_line_id': 'investing_activities'},
                'investing_net': {'name': '　　投资活动产生的现金流量净额', 'level': 1, 'parent_line_id': 'investing_activities'},
            'financing_activities': {'name': '三、筹资活动产生的现金流量：', 'level': 0},
                'investment_in': {'name': '吸收投资收到的现金', 'level': 1, 'parent_line_id': 'financing_activities'},
                'loan_in': {'name': '取得借款收到的现金', 'level': 1, 'parent_line_id': 'financing_activities'},
                'financing_activities_cash_in': {'name': '收到其他与筹资活动有关的现金', 'level': 1, 'parent_line_id': 'financing_activities'},
                'financing_in': {'name': '　筹资活动现金流入小计', 'level': 1, 'parent_line_id': 'financing_activities'},
                'loan_out': {'name': '偿还债务支付的现金', 'level': 1, 'parent_line_id': 'financing_activities'},
                'interest': {'name': '分配股利、利润或偿付利息支付的现金', 'level': 1, 'parent_line_id': 'financing_activities'},
                'financing_activities_cash_out': {'name': '支付其他与筹资活动有关的现金', 'level': 1, 'parent_line_id': 'financing_activities'},
                'financing_out': {'name': '　筹资活动现金流出小计', 'level': 1, 'parent_line_id': 'financing_activities'},
                'financing_net': {'name': '　　筹资活动产生的现金流量净额', 'level': 1, 'parent_line_id': 'financing_activities'},
            'exchange': {'name': '四、汇率变动对现金及现金等价物的影响', 'level': 0},
            'net_increase': {'name': '五、现金及现金等价物净增加额', 'level': 0},
                'opening_balance': {'name': '加：期初现金及现金等价物余额', 'level': 1, 'parent_line_id': 'net_increase'},
            'closing_balance': {'name': '六、期末现金及现金等价物余额', 'level': 0},
            'unclassified_activities': {'name': '未分类活动现金流量', 'level': 0},
                'unclassified_activities_cash_in': {'name': '现金流入', 'level': 1, 'parent_line_id': 'unclassified_activities'},
                'unclassified_activities_cash_out': {'name': '现金流出', 'level': 1, 'parent_line_id': 'unclassified_activities'},
        }