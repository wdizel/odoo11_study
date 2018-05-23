# -*- coding: utf-8 -*-
from odoo import api, fields, models

import logging

_logger = logging.getLogger(__name__)


class StoCustomer(models.Model):
    _name = 'res.partner'

    cars_ids = fields.One2many('fleet.vehicle', 'driver_id', string='Cars')
