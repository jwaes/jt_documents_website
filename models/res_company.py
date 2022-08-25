from odoo import api, fields, models, api, _


class ResCompany(models.Model):
    _inherit = "res.company"

    def _folder_id(self):
        foldr = self.env.company.product_folder
        return [('folder_id', '=', foldr.id)]

    product_document_website_tag = fields.Many2one('documents.tag', string="Product website document tag", domain=_folder_id,
                                     default=lambda self: self.env.ref('product_document_website_tag',
                                                                       raise_if_not_found=False))

    product_document_website_share = fields.Many2one('documents.share', string="Product website document share", domain=_folder_id,
                                     default=lambda self: self.env.ref('product_document_website_share',
                                                                       raise_if_not_found=False))
                                                               

