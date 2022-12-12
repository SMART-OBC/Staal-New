# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    @api.depends('product_id')
    def _compute_price_rights(self):
        if self:
            for rec in self:
                rec.is_read_only = self.env.user.has_group(
                    'sh_unitprice_access.sh_readonly_unit_price_group')

    is_read_only = fields.Boolean(compute='_compute_price_rights')
