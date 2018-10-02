# -*- coding: utf-8 -*-

from odoo import api, models, fields, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class CalendarEventMaster(models.Model):
    _inherit = 'calendar.event'

    # TODO: Створити можливість створювати сєйл ордери з каледаря (можливо)

    is_service = fields.Boolean('is_service')
    is_done = fields.Boolean('is_done')
    order_id = fields.Many2one('sale.order', 'Sale Order')
    sale_order_line = fields.Many2one('sale.order.line', 'Service')
    customer_id = fields.Many2one('res.partner', 'Customer')

    @api.multi
    def set_event_as_done(self):
        for rec in self:
            rec.is_done = True
            if rec.sale_order_line.task_id.project_id:
                if rec.user_id:
                    employee = self.env['hr.employee'].search([('user_id', '=', rec.user_id)], limit=1)

                    # TODO: Треба створити додаткову фільтрацію по емплоерах, оскільки їх може бути декілька прив'язаних до юзера

                    if employee:
                        task = rec.sale_order_line.task_id
                        project = rec.sale_order_line.task_id.project_id
                        timesheet = self.env['account.analytic.line'].search([])
                        timesheet.sudo().create({
                                                    'date': rec.stop,
                                                    'name': rec.name,
                                                    'project_id': project.id,
                                                    'task_id': task.id,
                                                    'employee_id': employee.id,
                                                    'unit_amount': rec.duration,
                                                })

            # TODO: Необхідно окремо реалізувати механізм контролю наявності таски, проєкта і т.д.

            else:
                raise UserError(_("There is no related project to this meeting."))
