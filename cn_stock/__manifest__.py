# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'cn Inventory',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'author': "He Jian",
    'category': 'Inventory/Inventory',
    'depends': ['stock'],
    'demo': [
        'data/stock_demo_pre.xml',
        'data/stock_demo.xml',
    ],
    'data': [
        'data/stock_data.xml',
        'data/cn_stock_demo.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
