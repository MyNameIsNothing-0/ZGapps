# -*- coding: utf-8 -*-
{
    'name': "Website Preloader",

    'summary': """
            Add a stylish preloader to your Odoo website.
        """,

    'description': """
        Enhance your website with a customizable preloader.
    """,

    'author': "Zero Gravity",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',
    'license': 'LGPL-3',
    'price': 5.00,
    'currency': 'USD',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        
        'web.assets_frontend': [
        ],
    },
    'images': [
        'static/description/banner.png',
    ]
}
