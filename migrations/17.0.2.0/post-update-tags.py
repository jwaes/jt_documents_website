import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):
    
    ProductDocument = util.env(cr)['product.document']
    DocumentsDocument = util.env(cr)['documents.document']

    website_tag = util.env(cr).user.company_id.product_document_website_tag
    _logger.info("Website tag is %s ", website_tag.name)
    attach_ids = DocumentsDocument.search([['tag_ids', 'in', website_tag.id]]).attachment_id.ids
    ids = ProductDocument.search([['ir_attachment_id', 'in', attach_ids ]]).ids



    for record in util.iter_browse(ProductDocument, ids):
        _logger.info("Product document website %s", record.name)
        if record.res_model == 'product.template':
            _logger.info("template is ok")
            record.shown_on_product_page = True
        elif record.res_model == 'product.product':
            _logger.info("variant is problematic")
            product = util.env(cr)[record.res_model].browse(record.attachment_id.id)
            record.res_model = 'product.template'
            record.res_id = product.product_tmpl_id.id
            record.shown_on_product_page = True