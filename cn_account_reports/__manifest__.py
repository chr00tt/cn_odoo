# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'cn Accounting Reports',
    'author': "He Jian",
    'category': 'Accounting/Accounting',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'depends': [
        'account_reports',
        'cn_account',
    ],
    'data': [
        'data/profit_and_loss.xml',
    ],
    'auto_install': True,
    'installable': True,
    'license': 'LGPL-3',
}
