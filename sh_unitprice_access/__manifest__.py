# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Sales Price Access",
    "author": "Softhealer Technologies",
    "license": "OPL-1",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Sales",
    "summary": "Restrict To Change Unit Price Extra Access Rights In Unit Price Read Only Unit Price Access Unit Price Management Restrict To Change Unit Price Extra Access Rights Product Unit Price Limitation Unit Price Restrict Odoo",
    "description": """Do you want to manage the unit price? The manager can set the unit price and everyone can't change the unit price. This module provides read-only access to a particular salesperson for which you don' want to allow them to edit the unit price in the product. """,
    "version": "15.0.1",
    "depends": ["sale_management"],
    "application": True,
    "data": [
        'security/unit_price_security.xml',
        'views/sale_order_views.xml',
    ],
    "images": ["static/description/background.png", ],    
    "auto_install": False,
    "installable": True,
    "price": 15,
    "currency": "EUR"
}
