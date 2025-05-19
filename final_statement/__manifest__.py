# -*- coding: utf-8 -*-
{
    'name': 'Final Statement',
    'version': '17.0.0.0.0',
    'summary': '',
    'description': '',
    'author': 'Jaffar',
    'website': 'https://yourwebsite.com',
    'category': 'Custom',
    'depends': ['base','purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/final_statement.xml',
        'views/action.xml',
        'views/menu.xml',
        'report/report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}