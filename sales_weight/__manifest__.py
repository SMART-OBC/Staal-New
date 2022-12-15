# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales Weight',
    'version': '1.0.4 ',
    'category': 'Sale ',
    'sequence': 20,
    'summary': 'Places weight and weight total',
    'description': "",
    'depends': ['base','sale','account'],
    'data': [
        'views/account_move_line.xml',
        'views/sale_order.xml',
        'report/customer_invoice_report.xml',
        'report/picking_invoice_report.xml',
        'report/picking_invoice_report_templates.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'qweb': [],
    'website': '',
}
