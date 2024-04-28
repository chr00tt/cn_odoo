# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Invoicing',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'author': "He Jian",
    'category': 'Accounting/Accounting',
    'depends' : ['account'],
    'data': [
        'data/account_data.xml',
        'data/cn_account.xml',
        'data/account.account.tag.csv',
        'data/account.account.template.csv',
        'data/cn_account_post.xml',
    ],
    'demo': [
        'data/cn_account_demo.xml',
        'data/account_account_demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
