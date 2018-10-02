# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
import logging

_logger = logging.getLogger(__name__)


class SaleOrderProductMaster(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_confirm(self):
        for r in self:
            if r.order_line:
                for rec in r.order_line:
                    calendar = self.env['calendar.event'].search([])
                    if rec.product_id.accessory_product_ids:
                        # TODO: Можливо додати функціонал запобіганню забвоювання товарів, але це під питанням
                        for accessory in rec.product_id.accessory_product_ids:
                            r.order_line.sudo().create({
                                                        'order_id': r.id,
                                                        'product_id': accessory.id,
                                                        })
                    if rec.master_ids and rec.service_start_datetime:
                        for master in rec.master_ids:
                            if master.user_id:
                                calendar.sudo().create({
                                                        'name': rec.name,
                                                        'start': rec.service_start_datetime,
                                                        'allday': False,
                                                        'stop': rec.end_date,
                                                        'start_datetime': rec.service_start_datetime,
                                                        'duration': rec.product_uom_qty,
                                                        'privacy': 'public',
                                                        'show_as': 'busy',
                                                        'user_id': master.user_id.id,
                                                        'is_service': True,
                                                        'order_id': r.id,
                                                        'sale_order_line': rec.id,
                                                        'customer_id': r.partner_id.id,
                                                        'partner_ids': [(6, 0, [r.partner_id.id])],
                                                       })

            super(SaleOrderProductMaster, self).action_confirm()

            invoice = {
                        'name': _('Invoice Order'),
                        'type': 'ir.actions.act_window',
                        'res_model': 'sale.advance.payment.inv',
                        'view_type': 'form',
                        'view_mode': 'form',
                        'target': 'new',
                      }

            return invoice
