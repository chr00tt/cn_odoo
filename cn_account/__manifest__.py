# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Invoicing',
    'author': "He Jian",
    'category': 'Invoicing Management',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'depends' : ['account'],
    'data': [
        'data/account_account_type.xml',
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/enterprise/enterprise_account.xml',
        'data/enterprise/account.account.template.csv',
        # 'data/enterprise/account.group.csv',
        'data/enterprise/enterprise_account_post.xml',
        'data/administrative_institution/administrative_institution_account.xml',
        'data/administrative_institution/account.account.template.csv',
        'data/administrative_institution/account.group.csv',
        'data/administrative_institution/administrative_institution_account_post.xml',
    ],
    'demo': [
        'data/cn_account_demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
