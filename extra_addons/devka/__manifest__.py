# -*- coding: utf-8 -*-

{
    'name': 'DEV_KA',
    'author':   'Alexa',
    'maintainer': 'Alexa',
    'summary': 'Tools',
    'category': 'Tools',
    'website': 'http://www.hzsho.in.ua',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': ['base', 'web'],
    'data': [
        'views/dev_view.xml',
        'views/action_dev.xml',
        'views/release.xml',
        'security/ir.model.access.csv',
            ],
    'qweb': [
            "static/src/xml/base.xml",
            ],
    'installable': True,
    'auto_install': False
}
