# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class StoCars(models.Model):
    _inherit = 'fleet.vehicle'

    assignment_count = fields.Integer('Assinment count')
    department_id = fields.Many2one('hr.department', string='Department')

    @api.multi
    def create_assignment(self):
        for rec in self:
            x = self.env['project.task'].search([('car_id', '=', rec.id)])
            x.create({
                      'name': rec.license_plate,
                      'car_id': rec.id,
                      'partner_id': rec.driver_id.id,
                      'department_id': rec.department_id.id,
                     })

    @api.multi
    def unlink(self):
        for rec in self:
            x = self.env['project.task'].search([('car_id', '=', rec.id)])
            if x:
                raise ValueError('Close Assignment before deleting Car')
        return super(StoCars, self).unlink()


class StoTaskCars(models.Model):
    _inherit = 'project.task'

    car_id = fields.Many2one('fleet.vehicle', string='Car')
    department_id = fields.Many2one('hr.department', string='Department')

