# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'cn Inventory',
    'author': "He Jian",
    'description': "",
    'website': 'https://github.com/chr00tt/cn_odoo',
    'depends': ['stock'],
    'category': 'Inventory/Inventory',
    'demo': [
        'data/cn_stock_demo.xml',
    ],
    'data': [
        'data/stock_data.xml',
        'data/mail_template_data.xml',
        'data/default_barcode_patterns.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
