# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from datetime import timedelta
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class SaleOrderLineProductMaster(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    @api.depends('service_start_datetime', 'product_uom_qty')
    def _set_end_date(self):
        for r in self:
            if r.service_start_datetime:
                start = fields.Datetime.from_string(r.service_start_datetime)
                r.end_date = fields.Datetime.to_string(start + timedelta(hours=r.product_uom_qty))

    master_ids = fields.Many2many('hr.employee', string='Master')
    service_start_datetime = fields.Datetime(string="Date, time")
    end_date = fields.Datetime(string="Date, time", compute=_set_end_date, store=True)
    type = fields.Selection(related='product_id.type')

    @api.multi
    def open_calendar(self):
        for r in self:
            empl_attend_list = []
            my_view = self.env.ref('so_calendar_product_empl.view_calendar_event_masters_calendar')
            if r.master_ids:
                for record in r.master_ids:
                    if record.user_id:
                        x = record.user_id.partner_id.id
                        empl_attend_list.append(x)

            if not r.master_ids or len(empl_attend_list) == 0:
                if r.product_id.master_ids:
                    for record in r.product_id.master_ids:
                        if record.user_id:
                            x = record.user_id.partner_id.id
                            empl_attend_list.append(x)

                if not r.product_id.master_ids or len(empl_attend_list) == 0:
                    raise UserError(_("There is no related partner(s) to employees."))

            ctx = {'search_default_partner_ids': empl_attend_list}

            return {
                'name': 'Meetings',
                'type': 'ir.actions.act_window',
                'res_model': 'calendar.event',
                'views': [(my_view.id, 'calendar')],
                'view_mode': 'calendar',
                'view_type': 'calendar',
                'target': 'new',
                'context': ctx,
            }
