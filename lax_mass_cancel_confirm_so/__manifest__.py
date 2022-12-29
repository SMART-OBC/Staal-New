# -*- coding: utf-8 -*-
{
    'name': "Mass Cancel Confirm Sale Orders",
    'summary': """ This module allows to cancel Or confirm Quotations mass/bulk/multiple Sales Orders
            from the tree view.""",
    'author': "Laxicon Solution",
    'website': "www.laxicon.in",
    'sequence': 101,
    'support': 'info@laxicon.in',
    'category': 'Sales',
    'version': '15.0.1.0.0',
    'license': 'LGPL-3',
    'description': """ This module allow to cancle or confirm Sales Orders on Sale > Quotation.
    """,
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sales_orders_cancel_confirm_wizard.xml',
    ],
    'images':  ["static/description/banner.png"],
    'installable': True,
    'auto_install': False,
    'application': True,
}
