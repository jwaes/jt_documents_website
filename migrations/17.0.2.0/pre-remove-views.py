import logging
from odoo.upgrade import util


_logger = logging.getLogger(__name__)


def migrate(cr, version):

    views_to_remove = [
        'jt_documents_website.website_sale_product',
        'jt_documents_website.website_sale_product_documents',
    ]


    for view in views_to_remove:
        _logger.info("About to remove view %s", view)
        util.remove_view(cr, xml_id=view)
    
    util.remove_record(cr, xml_id='jt_documents_website.res_config_settings_view_form')

