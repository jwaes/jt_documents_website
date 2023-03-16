from odoo import api, fields, models
from os.path import splitext


class ProductProduct(models.Model):
    _inherit = "product.product"

    # product_website_document_ids = fields.One2many('documents.document', string='Variant website documents', compute='_compute_product_document_ids')
    product_document_website_ids = fields.One2many('documents.document', compute='_compute_product_document_website_ids', compute_sudo=True, string='foo')
    
    def _compute_product_document_website_ids(self):
        product_website_tag = self.env.user.company_id.product_document_website_tag
        product_website_share = self.env.user.company_id.product_document_website_share

        for record in self:
            product_documents = self.env['documents.document'].sudo().search([('res_model', '=', self._name), ('res_id', '=', self.id), ('type', '=', 'binary'), ]).filtered(lambda doc: product_website_tag in doc.tag_ids)
            product_template_documents = self.env['documents.document'].sudo().search([('res_model', '=', self.product_tmpl_id._name), ('res_id', '=', self.product_tmpl_id.id), ('type', '=', 'binary'), ]).filtered(lambda doc: product_website_tag in doc.tag_ids)
            all_docs = product_documents | product_template_documents
            record.product_document_website_ids = all_docs

            # for record in self:
            # record.full_url = "%s/document/share/%s/%s" % (record.get_base_url(), record.id, record.access_token)

    def _get_product_website_document_array(self):
        self.ensure_one()

        documents = []
        for doc in self.product_document_website_ids:
            ext = splitext(doc.name)[1].replace(".","").lower()
            documents.append({
                'id': doc.id,
                'name': doc.name,
                'file_extension': ext,
            })
        return documents

    def _has_product_website_documents(self):
        self.ensure_one()
        return len(self.product_document_website_ids) > 0

    # def _get_product_document_website_share(self):
    #     return self.env.user.company_id.product_document_website_share

