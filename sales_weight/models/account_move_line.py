

from odoo import api, fields, models, _


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    weight = fields.Float("Weight",compute="compute_weight")
    weight_total = fields.Float("Total Weight")

    @api.depends('weight')
    def compute_weight(self):
        for rec in self:
            rec.weight = rec.product_id.weight
            rec.weight_total = rec.weight * rec.quantity