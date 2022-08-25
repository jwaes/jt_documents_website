# -*- coding: utf-8 -*-
{
    'name': "jt_documents_website",

    'summary': "Public documents for products on webshop",

    'description': "",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'documents_product',
        'jt_product_properties_website',
        ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/document_views.xml',
        'views/website_sale_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'jt_documents_website/static/src/js/**/*',
        ],
    },      
}
