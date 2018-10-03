# -*- coding: utf-8 -*-

{
    'name': 'Custom Calendar SO Tuning',
    'author':   'Alexa',
    'maintainer': 'Alexa',
    'description': """
    done - в товарі (product.product) з типом послуга створити поля Майстер, який може надавати цю послугу /
    done - В sale.order.line створити поля Майстер, Дата надання послуги /
    done - action_confirm перевіряє accessory_product_ids та додає їх до SO /
    done - action_confirm викликає візард створення інвойсу /
    done - action_confirm створює подію в календарях майстрів /
    done - В sale.order.line додано посилання на календар майстрів /
    done - calendar.event створено кнопку 'DONE' що створює таймшит у конкретного майстра /
    """,
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
