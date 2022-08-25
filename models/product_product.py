from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    # product_website_document_ids = fields.One2many('documents.document', string='Variant website documents', compute='_compute_product_document_ids')
    product_document_website_ids = fields.One2many('documents.document', compute='_compute_product_document_website_ids', compute_sudo=True, string='foo')
    
    def _compute_product_document_website_ids(self):
        product_website_tag = self.env.user.company_id.product_document_website_tag
        product_website_share = self.env.user.company_id.product_document_website_share

        for record in self:
            blah = 1
            product_documents = self.env['documents.document'].sudo().search([('res_model', '=', self._name), ('res_id', '=', self.id), ('type', '=', 'binary'), ]).filtered(lambda doc: product_website_tag in doc.tag_ids)
            product_template_documents = self.env['documents.document'].sudo().search([('res_model', '=', self.product_tmpl_id._name), ('res_id', '=', self.product_tmpl_id.id), ('type', '=', 'binary'), ]).filtered(lambda doc: product_website_tag in doc.tag_ids)
            all_docs = product_documents | product_template_documents
            record.product_document_website_ids = all_docs

            # for record in self:
            # record.full_url = "%s/document/share/%s/%s" % (record.get_base_url(), record.id, record.access_token)