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
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/enterprise/enterprise_account.xml',
        'data/enterprise/account.account.template.csv',
        'data/enterprise/enterprise_account_post.xml',
        'data/administrative_institution/administrative_institution_account.xml',
        'data/administrative_institution/account.account.template.csv',
        'data/administrative_institution/administrative_institution_account_post.xml',
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
