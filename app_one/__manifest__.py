# -*- coding: utf-8 -*-
{
    'name': 'App One',
    'version': '1.0',
    'summary': 'A custom Odoo module for App One',
    'description': 'This is a custom module for Odoo 17, providing specific functionality for App One.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}