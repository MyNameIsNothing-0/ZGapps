# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Robin, Afra MP (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import http
from odoo.http import request


class DynamicDashboard(http.Controller):
    """Class to search and filter values in dashboard"""

    @http.route('/tile/details', type='json', auth='user')
    def tile_details(self, **kw):
        """Function to get tile details"""
        tile_id = request.env['dashboard.block'].sudo().browse(int(kw.get('id')))
        if tile_id:
            return {'model': tile_id.model_id.model, 'filter': tile_id.filter,
                    'model_name': tile_id.model_id.name}
        else:
            return False

    @http.route('/custom_dashboard/search_input_chart', type='json',
                auth="public", website=True)
    def dashboard_search_input_chart(self, search_input):
        """Function to filter search input in dashboard"""
        return request.env['dashboard.block'].search([
            ('name', 'ilike', search_input)]).ids

    # @http.route(_routes, type="http", auth="none", methods=["PATCH"], csrf=False)
    # def patch(self, model=None, action=None, **payload):
    #     """."""
    #     args = []

    #     payload = request.httprequest.data.decode()
    #     args = ast.literal_eval(payload)
    #     try:
    #         _id = int(id)
    #     except Exception as e:
    #         return invalid_response("invalid object id", "invalid literal %s for id with base" % id)
    #     try:
    #         record = request.env[model].sudo().search([("id", "=", _id)], limit=1)
    #         _callable = action in [method for method in dir(record) if callable(getattr(record, method))]
    #         if record and _callable:
    #             # action is a dynamic variable.
    #             res = getattr(record, action)(*args) if args else getattr(record, action)()
    #         else:
    #             return invalid_response(
    #                 "invalid object or method",
    #                 "The given action '%s ' cannot be performed on record with id '%s' because '%s' has no such method"
    #                 % (action, _id, model),
    #                 404,
    #             )
    #     except Exception as e:
    #         return invalid_response("exception", e, 503)
    #     else:
    #         return valid_response(res)

