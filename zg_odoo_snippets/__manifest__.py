# -*- coding: utf-8 -*-
{
    'name': "Odoo Title Snippet ",

    'summary': """
        Odoo title snippet""",

    'description': """
        Odoo Title Snippet
    """,

    'author': "Kanish",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
}
