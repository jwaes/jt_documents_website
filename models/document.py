import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class Document(models.Model):
    _inherit = 'documents.document'


    def write(self, vals):
        write_result = super(Document, self).write(vals)
        self._sync_product_document_website_share()
        return write_result

    def _sync_product_document_website_share(self):
        _logger.info('syncing product document website share')
        product_website_tag = self.env.user.company_id.product_document_website_tag
        product_website_share = self.env.user.company_id.product_document_website_share

        for doc in self:
            if product_website_tag in doc.tag_ids:
                if doc not in product_website_share.document_ids:
                    doc.add_to_documents_website_share()
            else:
                if doc in product_website_share.document_ids:
                    doc.remove_from_documents_website_share()


    def add_to_documents_website_share(self):
        product_website_share = self.env.user.company_id.product_document_website_share
        for doc in self:
            product_website_share.write({'document_ids':[(4,doc.id,_)]})

    def remove_from_documents_website_share(self):
        product_website_share = self.env.user.company_id.product_document_website_share
        for doc in self:
            product_website_share.write({'document_ids':[(3,doc.id,_)]})            
