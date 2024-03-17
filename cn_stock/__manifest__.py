# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': '中国 库存',
    'author': "He Jian",
    'category': 'Inventory/Inventory',
    'depends': ['stock'],
    'data': [
        'data/stock_data.xml',
        'data/mail_template_data.xml',
        'data/default_barcode_patterns.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': '',
}
