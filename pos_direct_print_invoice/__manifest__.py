# -*- coding: utf-8 -*-
###############################################################################
#
#   Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#   Copyright (C) 2016-today Geminate Consultancy Services (<http://geminatecs.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    "name": "Point of Sale Direct Print Invoice",
    'version': '15.0.0.1',
    'author': 'Geminate Consultancy Services',
    'company': 'Geminate Consultancy Services',
    'summary': 'Allows you to print invoice directly from receipt screen of point of sale.',
    'license': 'Other proprietary',
    "description":
        """
       		This module will print invoice directly from receipt screen of point of sale. it will help you to print receipts and invoices both together from the same screen.
        """,
    'website': 'https://www.geminatecs.com/',
    "depends": ['web','point_of_sale'],
    'category': 'Point of Sale',
    'data': [
          'views/pos_assets.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_direct_print_invoice/static/src/js/pos_direct_print_invoice.js',
        ],
        'web.assets_qweb': [
            'pos_direct_print_invoice/static/src/xml/*.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    'installable': True,   
    'auto_install': False,
    'price': 39.99,
    'currency': 'EUR'
}
