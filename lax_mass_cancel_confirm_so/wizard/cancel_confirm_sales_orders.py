from odoo import api, models, _
from odoo.exceptions import UserError


class CancelSalesOrders(models.TransientModel):
    _name = 'cancel.sales.orders'

    def cancel_sales_orders(self):
        """ cancel multiple sales orders from the tree view."""
        cancel_sale_order = self.env['sale.order'].browse(
            self._context.get('active_ids'))
        cancel_sale_order.action_cancel()
        return True


class ConfirmSalesOrders(models.TransientModel):
    _name = 'confirm.sales.orders'

    def confirm_sales_order(self):
        """ confirm multiple sales orders from the tree view."""
        confirm_sale_order = self.env['sale.order'].browse(
            self._context.get('active_ids'))
        confirm_sale_order.action_confirm()
        return True
