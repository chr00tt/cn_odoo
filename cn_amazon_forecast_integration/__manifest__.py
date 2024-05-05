# -*- coding: utf-8 -*-
{
    'name': "Amazon Forecast Integration",
    'author': "He Jian",
    'category': 'Warehouse',
    'website': 'https://github.com/chr00tt/cn_odoo',
    'depends': ['amazon_forecast_integration'],
    'assets': {
        'web.assets_backend': [
            ('replace', 'https://cdn.jsdelivr.net/npm/chart.js', 'https://fastly.jsdelivr.net/npm/chart.js'),
            ('replace', 'https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js', 'https://fastly.jsdelivr.net/npm/chartjs-adapter-date-fns@3.0.0/dist/chartjs-adapter-date-fns.bundle.min.js'),
        ],
    },
    'installable': True,
    'auto_install': True,
    'application': False,
    'license': 'AGPL-3',
}
