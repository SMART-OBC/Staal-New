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
from odoo import models,fields,_,api,tools
import json

class PointOfSaleInv(models.Model):
    _inherit ='pos.config'
    
    direct_print_invoice = fields.Boolean("Direct Print Invoice")
    
class PosOrderInv(models.Model):
    _inherit = 'pos.order'
    
    def direct_print_invoice(self, pos_reference):
        pos = self.sudo().search([('pos_reference','=',str(pos_reference))],limit=1)
        if pos:
            res = pos.action_pos_order_invoice()
            if res and 'res_id' in res and res.get('res_id'):
                account_move = self.env['account.move'].sudo().browse(int(res.get('res_id')))
                if account_move:
                  invoice_tax_line_ids=[]
                  invoice_data = []
                  tax_data = []
                  if account_move:
                      for line_id in account_move.invoice_line_ids:
                          tax_name = ''
                          for tax_ids in line_id.tax_ids:
                              tax_name = tax_name + tax_ids.name + ','
                          line_data = {
                                       'product_name': line_id.name,
                                       'quantity': round(line_id.quantity,2),
                                       'quantity_uom':line_id.product_uom_id.name,
                                       'price_unit':round(line_id.price_unit,2),
                                       'discount':line_id.discount,
                                       'taxes' : tax_name,
                                       'sub_total': round(line_id.price_subtotal,2),
                                       'tax_amount':line_id.tax_ids
                                       }
                          invoice_data.append(line_data)
                      for tax_id in account_move.invoice_line_ids:
                          t_data = {
                                    'name' : tax_id.name,
                                    'amount':tax_id.price_unit - tax_id.price_subtotal
                                    }
                          tax_data.append(t_data)
                      return {
                              'currency_id': account_move.currency_id.symbol + ' ',
                              'inv_id': account_move.id,
                              'inv_name' : account_move.ref,
                              'inv_origin': account_move.invoice_origin,
                              'inv_date_invoice': account_move.invoice_date,
                              'inv_date_due' : account_move.invoice_date_due,
                              'inv_number' : account_move.name,
                              'invoice_data': invoice_data,
                              'tax_data': json.loads(account_move.tax_totals_json).get('formatted_amount_total'),
                              'amount_untaxed': round(account_move.amount_untaxed,2),
                              'amount_total': round(account_move.amount_total,2)
                            }
        return False
