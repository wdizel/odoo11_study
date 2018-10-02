# -*- coding: utf-8 -*-

{
    'name': 'Custom Calendar SO Tuning',
    'author':   'Alexa',
    'maintainer': 'Alexa',
    'summary': 'Tools',
    'category': 'Tools',
    'website': 'http://www.simbioz.ua',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
                'base',
                'web',
                'product',
                'sale',
                'calendar',
                'hr',
                'hr_timesheet'
               ],
    'data': [
                'views/product.xml',
                'views/so.xml',
                'views/calendar_event.xml',
            ],
    'qweb': [

            ],
    'installable': True,
    'auto_install': False
}
