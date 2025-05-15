# -*- coding: utf-8 -*-
{
    'name': 'Count Module',
    'version': '17.0.0.1.0',
    'summary': 'A custom Odoo module for Count Module',
    'description': 'This is a custom module for Odoo 17, providing specific functionality for Count Module.',
    'author': 'Jaffar',
    'website': 'https://yourwebsite.com',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/vote_option.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}