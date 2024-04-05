# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Invoicing',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'author': "He Jian",
    'category': 'Accounting',
    'depends' : ['account'],
    'data': [
        'data/cn_account_coa_chart_data.xml',
        'data/data_account_type.xml',
        'data/account.account.template.csv',
        'data/cn_account_coa_post.xml',
    ],
    'installable': True,
    'auto_install': True,
}
