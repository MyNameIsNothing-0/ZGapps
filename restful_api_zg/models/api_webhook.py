# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import models, fields, api


class ApiWebhook(models.Model):
    _name = 'odoo.api.webhook'
    _description = 'Odoo Api Webhook'

    name = fields.Char("Webhook Name")
    description = fields.Text(translate=True)
    webhook_url = fields.Char("Webhook URL")
    full_webhook_url = fields.Char("Full Webhook URL",compute="_compute_webhook_url")
    response_count = fields.Integer("Response Count",compute="_compute_count")
    sequence = fields.Integer("Response Count")
    color = fields.Char('Color')
    webhook_response_ids = fields.One2many("odoo.api.webhook.response","webhook_id",string="Response data")
    _sql_constraints = [
        ('webhook_url_unique_constraint', 'UNIQUE(webhook_url)', 'Webhook URL must be unique!'),
    ]
    def test_api_method(self):
        print("API trigger Success...........")
        return "API Method"
    def _compute_count(self):
        for rec in self:
            rec.response_count = len(rec.webhook_response_ids)
    def _compute_webhook_url(self):
        for rec in self:
            base_url = self.env['ir.config_parameter'].get_param('web.base.url')
            rec.full_webhook_url = f"{base_url}/webhook/z3/{rec.webhook_url}"

class ApiWebhookResponse(models.Model):
    _name = 'odoo.api.webhook.response'
    _description = 'Odoo Api Webhook Respomse'
    name = fields.Char("Response Reference")
    webhook_id = fields.Many2one('odoo.api.webhook',string="Webhook Id")
    header_data = fields.Text("Header Data")
    response_data = fields.Text("Response Data")
    color = fields.Char('Color Index')
