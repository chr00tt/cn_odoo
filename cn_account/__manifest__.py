# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Invoicing',
    'author': "He Jian",
    'category': 'Accounting/Accounting',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'depends' : ['account'],
    'data': [
        'data/cn_account.xml',
        'data/account.account.template.csv',
        'data/cn_account_post.xml',
    ],
    'demo': [
        'data/cn_account_demo.xml',
        'demo/demo_company.xml',
        'data/account_account_demo.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
