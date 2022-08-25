from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    product_document_website_tag = fields.Many2one('documents.tag', related='company_id.product_document_website_tag', readonly=False,
                                     string="Product website document tag")

    product_document_website_share = fields.Many2one('documents.share', related='company_id.product_document_website_share', readonly=False,
                                     string="Product website document share")

