# -*- coding: utf-8 -*-
from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)


class ProductMaster(models.Model):
    _inherit = 'product.template'

    master_ids = fields.Many2many('hr.employee', string='Masters')