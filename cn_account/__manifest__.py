# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Invoicing',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'author': "He Jian",
    'category': 'Accounting/Accounting',
    'depends' : ['account'],
    'data': [
        'data/cn_account_coa.xml',
        'data/account.account.template.csv',
        'data/cn_account_coa_post.xml',
    ],
    'demo': [
        'data/cn_account_demo.xml',
        'demo/demo_company.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
