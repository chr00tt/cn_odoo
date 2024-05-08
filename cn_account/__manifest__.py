# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Invoicing',
    'author': "He Jian",
    'category': 'Accounting/Accounting',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'depends' : ['account'],
    'data': [
        'data/account_data.xml',
        'data/cn_account.xml',
        'data/account.account.tag.csv',
        'data/account.account.template.csv',
        'data/cn_account_post.xml',
    ],
    'demo': [
        'demo/cn_account_demo.xml',
        'demo/account.account.csv',
        'demo/analytic_account_demo.xml',
        'demo/res.bank.csv',
        'demo/res.partner.bank.csv',
        'demo/account.journal.csv',
        'demo/account.move.csv',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
