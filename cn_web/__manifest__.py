# -*- coding: utf-8 -*-

{
    'name': 'cn Web',
    'author': 'He Jian',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'category': 'Hidden',
    'depends': ['web'],
    'auto_install': True,
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'cn_web/static/src/views/**/*',
        ],
    },
    'license': 'LGPL-3',
}
