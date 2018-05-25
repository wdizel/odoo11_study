# -*- coding: utf-8 -*-

{
    'name': 'STO Customers / Cars',
    'version': '11.0.1.0.0',
    'category': 'Fleet service',
    'license': 'AGPL-3',
    'author': 'Simbioz',
    'maintainer': 'Simbioz',
    'website': 'http://www.simbioz.ua',
    'depends': ['base', 'fleet'],
    'data': [
                'wizards/assignment_wizard.xml',
                'views/department.xml',
                'views/customer.xml',
                'views/task.xml',
             ],
    'installable': True,
    'application': True,
    'sequence': 0,
}
