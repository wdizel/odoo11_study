# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class StoDepartmentCars(models.Model):
    _inherit = 'hr.department'

    post_id = fields.Many2one('project.project', string='Post')
