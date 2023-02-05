# -*- coding: utf-8 -*-
# from odoo import http


# class WebsitePreloaderZg(http.Controller):
#     @http.route('/website_preloader_zg/website_preloader_zg', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_preloader_zg/website_preloader_zg/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_preloader_zg.listing', {
#             'root': '/website_preloader_zg/website_preloader_zg',
#             'objects': http.request.env['website_preloader_zg.website_preloader_zg'].search([]),
#         })

#     @http.route('/website_preloader_zg/website_preloader_zg/objects/<model("website_preloader_zg.website_preloader_zg"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_preloader_zg.object', {
#             'object': obj
#         })
