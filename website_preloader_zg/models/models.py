# -*- coding: utf-8 -*-
from odoo import api, fields, models, modules


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_preloader_enable = fields.Boolean(string="Enable", help='Enable',default=False)
    website_preloader_image = fields.Binary(string="Image", help='Select Background Image For Login Page')
    website_preloader_color = fields.Char(string="Preloader Color", help="Choose your loader color")
    website_preloader_bg_color = fields.Char(string="Preloader Background Color", help="Choose your Background color")
    website_preloader_animation = fields.Selection(
        [('loader_three', 'Three Ring'),
        ('fade_ring_loader', 'Ring'),
        ('loader_ring', 'Ring 2'),
        ('loader_timer_load', 'Timer'),
        ('loader_tea_cup_load', 'Tea Cup'),
        ('loader_clock_load', 'Clock'),
        ('loader_image_logo_spinner', 'Image Logo'),
        ('loader_block_move_spinner', 'Moving Block'),
        ('loader_square_loading', 'Square animation'),
        ], 
        default='loader_three', 
        help='Loader Animation',
        tracking=True
        )
    

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        # image_id = int(self.env['ir.config_parameter'].sudo().get_param('login_background__zg.login_background_image'))
        res.update(
            website_preloader_enable=self.env['ir.config_parameter'].sudo().get_param('website_preloader_zg.website_preloader_enable'),
            website_preloader_image=self.env['ir.config_parameter'].sudo().get_param('website_preloader_zg.website_preloader_image'),
            website_preloader_color=self.env['ir.config_parameter'].sudo().get_param('website_preloader_zg.website_preloader_color'),
            website_preloader_bg_color=self.env['ir.config_parameter'].sudo().get_param('website_preloader_zg.website_preloader_bg_color'),
            website_preloader_animation=self.env['ir.config_parameter'].sudo().get_param('website_preloader_zg.website_preloader_animation'),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        website_preloader_enable = self.website_preloader_enable or False
        set_website_preloader_image = self.website_preloader_image or False
        website_preloader_color = self.website_preloader_color or False
        website_preloader_bg_color = self.website_preloader_bg_color or False
        website_preloader_animation = self.website_preloader_animation or False
        param.set_param('website_preloader_zg.website_preloader_enable', website_preloader_enable)
        param.set_param('website_preloader_zg.website_preloader_image', set_website_preloader_image)
        param.set_param('website_preloader_zg.website_preloader_color', website_preloader_color)
        param.set_param('website_preloader_zg.website_preloader_bg_color', website_preloader_bg_color)
        param.set_param('website_preloader_zg.website_preloader_animation', website_preloader_animation)
