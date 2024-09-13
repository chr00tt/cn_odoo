# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Invoicing',
    'author': "He Jian",
    'category': 'Accounting',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'depends' : ['account'],
    'data': [
        'data/data_account_type.xml',
        'data/account.account.tag.csv',
        'data/account.tax.group.csv',
        'data/enterprise/enterprise_account.xml',
        'data/enterprise/account.account.template.csv',
        'data/enterprise/enterprise_account_post.xml',
        'data/enterprise/account_chart_template_data.yml',
        'data/administrative_institution/administrative_institution_account.xml',
        'data/administrative_institution/account.account.template.csv',
        'data/administrative_institution/account.group.csv',
        'data/administrative_institution/administrative_institution_account_post.xml',
        'data/administrative_institution/account_chart_template_data.yml',
    ],
    'demo': [
        'data/cn_account_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
}
