# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class StoWizardCars(models.TransientModel):
    _name = 'assignment.create.wizard'

    @api.multi
    def _default_car_id(self):
        x = self.env['fleet.vehicle'].browse(self._context.get('active_id'))
        return x

    car_id = fields.Many2one('fleet.vehicle', string='Car', default=_default_car_id)
    post_id = fields.Many2one('project.project', string='Post')
    department_id = fields.Many2one('hr.department',
                                    string='Department',
                                    domain="[('post_id', '=', post_id)]")
    master_id = fields.Many2one('hr.employee',
                                string='Master',
                                domain="[('department_id', '=', department_id)]")

    @api.multi
    def save_close(self):
        x = self.env['project.task'].browse()
        x.create({
          'project_id': self.post_id.id,
          'name': self.car_id.license_plate,
          'car_id': self.car_id.id,
          'partner_id': self.car_id.driver_id.id,
          'department_id': self.department_id.id,
          'employee_id': self.master_id.id,
        })
