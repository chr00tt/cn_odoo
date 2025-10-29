# -*- coding: utf-8 -*-

from odoo import api, fields, models, modules, tools, _

class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def _update_translations(self, filter_lang=None, overwrite=False):
        super()._update_translations(filter_lang=filter_lang, overwrite=True)
