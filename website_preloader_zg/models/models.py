# -*- coding: utf-8 -*-
from odoo import api, fields, models, modules


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_preloader_image = fields.Binary(string="Image", help='Select Background Image For Login Page')

    

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # image_id = int(self.env['ir.config_parameter'].sudo().get_param('login_background__zg.login_background_image'))
        res.update(
            website_preloader_image=self.env['ir.config_parameter'].sudo().get_param('website_preloader_zg.website_preloader_image'),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        set_website_preloader_image = self.website_preloader_image or False
        param.set_param('website_preloader_zg.website_preloader_image', set_website_preloader_image)
