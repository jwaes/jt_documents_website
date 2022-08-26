from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController
from os.path import splitext

class WebsiteSaleStockDocumentsVariantController(WebsiteSaleVariantController):
    @http.route()
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kw):
        kw['context'] = kw.get('context', {})
        kw['context'].update(website_sale_product_documents=True)
        combination = super().get_combination_info_website(product_template_id, product_id, combination, add_qty, **kw)

        product = request.env['product.product'].sudo().browse(combination['product_id']);
        product_website_share = request.env.user.company_id.product_document_website_share

        documents = []
        for doc in product.product_document_website_ids:
            ext = splitext(doc.name)[1].replace(".","")
            documents.append({
                'id': doc.id,
                'name': doc.name,
                'file_extension': ext,
            })

        documents_view = request.env['ir.ui.view']._render_template('jt_documents_website.website_sale_product_documents', values={
            'has_product_documents': len(documents) > 0,
            'documents': documents,
            'product_website_share': product_website_share,
        })

        combination['product_documents'] = documents_view

        return combination