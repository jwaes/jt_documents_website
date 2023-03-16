from odoo import api, fields, models
from os.path import splitext

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def product_website_documents(self):
        product_website_tag = self.env.user.company_id.product_document_website_tag
        product_template_documents = self.env['documents.document'].search([('res_model', '=', self._name), ('res_id', '=', self.id), ('type', '=', 'binary'), ]).filtered(lambda doc: product_website_tag in doc.tag_ids)
        return product_template_documents


    def _get_product_website_document_array(self):
        self.ensure_one()

        documents = []
        for doc in self.product_website_documents():
            ext = splitext(doc.name)[1].replace(".","").lower()
            documents.append({
                'id': doc.id,
                'name': doc.name,
                'file_extension': ext,
            })
        return documents

    def _has_product_website_documents(self):
        self.ensure_one()
        return len(self.product_website_documents()) > 0

    def _get_product_document_website_share(self):
        return self.env.user.company_id.product_document_website_share        