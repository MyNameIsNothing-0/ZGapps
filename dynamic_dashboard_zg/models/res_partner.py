from odoo import api, fields, models


class ResPartner(models.Model):
    """Class to create new dashboard menu"""
    _inherit = "res.partner"

    @api.model
    def action_get_chart_data(self):
        return {
        "x":["name 1","name 2","name 3","jeeva 1","sakthi","pavi","logu","saran"],
        "y":[31,24,35,24,45,35,24,45],
        }
