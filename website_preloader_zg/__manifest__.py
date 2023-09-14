# -*- coding: utf-8 -*-
{
    'name': "Website Preloader",

    'summary': """

        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Zero Gravity",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'price': 1.00,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        
        'web.assets_frontend': [
            'website_preloader_zg/static/src/css/*.css',
        ],
    },
    'images': [
        'static/description/banner.png',
    ]
}
