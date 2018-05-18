# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import datetime


class module_dependency(models.Model):
    _inherit = 'ir.module.module.dependency'

    author = fields.Char('Author', compute='_compute_author')

    @api.one
    @api.depends('depend_id.author')
    def _compute_author(self):
        self.author = self.depend_id.author or 'unknown'

    @api.multi
    def dt_button_install(self):
        module_obj = self.env['ir.module.module']
        module_id = module_obj.search([('name', '=', self.name)])
        module_id.button_immediate_install()
        return True

    @api.multi
    def dt_button_immediate_upgrade(self):
        module_obj = self.env['ir.module.module']
        module_id = module_obj.search([('name', '=', self.name)])
        module_id.button_immediate_upgrade()
        return True

    @api.multi
    def dt_button_uninstall(self):
        module_obj = self.env['ir.module.module']
        module_id = module_obj.search([('name', '=', self.name)])
        module_id.button_immediate_uninstall()
        return True


class module(models.Model):
        _inherit = 'ir.module.module'

        inst_id = fields.Many2one('ir.module.module')
        upg_id = fields.Many2one('ir.module.module')
        uninst_id = fields.Many2one('ir.module.module')
        inst2_id = fields.Many2one('ir.module.module')
        upg2_id = fields.Many2one('ir.module.module')
        uninst2_id = fields.Many2one('ir.module.module')