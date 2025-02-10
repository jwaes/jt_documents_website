import VariantMixin from "@website_sale/js/sale_variant_mixin";

const originalOnChangeCombination = VariantMixin._onChangeCombination;
VariantMixin._onChangeCombinationProductDocuments = function (ev, $parent, combination) {
    let product_id = 0;
    // needed for list view of variants
    
    if ($parent.find('input.product_id:checked').length) {
        product_id = $parent.find('input.product_id:checked').val();
    } else {
        product_id = $parent.find('.product_id').val();
    }
    const isMainProduct = combination.product_id &&
        ($parent.is('.js_main_product') || $parent.is('.main_product')) &&
        combination.product_id === parseInt(product_id);

    if (!this.isWebsite || !isMainProduct) {
        // return;
    }

    $('div.product_documents').html(combination.product_documents);

    $("a.track_document_download").click(function(){

        let file_name = $(this).attr('data-name');
        let file_extension = $(this).attr('data-file-extension');
        let file_url = $(this).attr('href');
        
        const trackingInfo = {
            'file_name': file_name,
            'link_url': file_url,
            'file_extension': file_extension,
        };

        if(window.gtag){
            window.gtag("event", "file_download", {
                file_name: file_name,
                link_url: file_url,
                file_extension: file_extension,
            });
        }

    });
    originalOnChangeCombination.apply(this, [ev, $parent, combination]);
};

export default VariantMixin;