from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def product_website_documents(self):
        product_website_tag = self.env.user.company_id.product_document_website_tag
        product_template_documents = self.env['documents.document'].search([('res_model', '=', self._name), ('res_id', '=', self.id), ('type', '=', 'binary'), ]).filtered(lambda doc: product_website_tag in doc.tag_ids)
        return product_template_documents    