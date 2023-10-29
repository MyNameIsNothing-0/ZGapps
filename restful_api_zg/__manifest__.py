{
    "name": "RESTFUL API & Webhooks",
    "version": "1.2.0",
    "category": "API",
    "author": "Kanish Info",
    "website": "",
    "summary": "RESTFUL API & Webhooks",
    "support": "kanish230523@gmail.com",
    'category': 'Website',
    'version': '0.1',
    'license': 'LGPL-3',
    'price': 20.00,
    'currency': 'USD',

    "description": """ RESTFUL API & Webhook Endpoints For Odoo 15, 16
""",
    "depends": ["web", "base_setup"],
    "data": [
        "views/ir_model.xml", 
        "views/res_users.xml", 
        "views/api_webhook_views.xml", 
        "views/api_webhook_response_views.xml",
        "security/ir.model.access.csv",
        ],
    "images": ["static/description/banner.gif"],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
}
