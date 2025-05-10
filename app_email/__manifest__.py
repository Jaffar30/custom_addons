# -*- coding: utf-8 -*-
{
    'name': 'App Email',
    'version': '17.0.0.1.0',
    'summary': 'A custom Odoo module for App Email',
    'description': 'This is a custom module for Odoo 17, providing specific functionality for App Email.',
    'author': 'Jaffar',
    'website': 'https://yourwebsite.com',
    'category': 'Custom',
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/action.xml',
        'data/emp_cron.xml', 
        'data/email_template.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}