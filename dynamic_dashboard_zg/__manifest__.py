# -*- coding: utf-8 -*-
{
    'name': "Dynamic Dashboard",

    'summary': """
            An Odoo app designed to create and manage dynamic dashboards within the Odoo ERP system.
        """,

    'description': """
        The "Dynamic Dashboard" app is a powerful tool that empowers 
        users to create customizable and interactive dashboards in Odoo. 
        It allows users to visualize and analyze key performance indicators (KPIs), business metrics, 
        and other critical data in a visually appealing and informative manner.
    """,

    'author': "Zero Gravity",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'license': 'LGPL-3',
    'price': 4.00,
    'currency': 'USD',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/dashboard_views.xml',
        'views/dynamic_block_views.xml',
        'views/dashboard_menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'https://cdn.jsdelivr.net/npm/apexcharts',
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css",
            'dynamic_dashboard_zg/static/lib/css/gridstack.min.css',
            'dynamic_dashboard_zg/static/src/css/dynamic_dashboard.css',
            'dynamic_dashboard_zg/static/src/scss/dynamic_dashboard.scss',
            "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css",
            'https://cdnjs.cloudflare.com/ajax/libs/gridstack.js/0.2.6/gridstack.min.js',
            'https://cdn.jsdelivr.net/npm/chart.js',
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/jqueryui-touch-punch/0.2.3/jquery.ui.touch-punch.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/bootbox.js/4.4.0/bootbox.min.js",
            'https://cdnjs.cloudflare.com/ajax/libs/jspdf/1.5.3/jspdf.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js',
            'dynamic_dashboard_zg/static/src/js/dynamic_dashboard.js',
            'dynamic_dashboard_zg/static/src/xml/dynamic_dashboard_template.xml',
            'https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700',
        ],
    },
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}
