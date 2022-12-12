odoo.define('pos_direct_print_invoice.pos_direct_print_invoice_js', function (require) {
"use strict";
	
	const ReceiptScreen = require('point_of_sale.ReceiptScreen');
	const Registries = require('point_of_sale.Registries');
	var ajax = require('web.ajax');
	var core = require('web.core');
	var QWeb = core.qweb;
	var _t = core._t;
	var rpc = require('web.rpc');
	var models = require('point_of_sale.models');
	models.load_fields('res.company',['street','street2','city','state_id','phone','zip','currency_id', 'email', 'website', 'company_registry', 'vat', 'name', 'phone', 'partner_id' , 'country_id', 'tax_calculation_rounding_method']);

	const PrintDirectInvoice = ReceiptScreen =>
	    class extends ReceiptScreen {
	    	
	    	async PrintDirectInvoice() {
                var self= this;
                var order = this.currentOrder;
				if(order && order.name && this.env.pos.config.invoice_journal_id){
					this.rpc({
		                model :'pos.order',
		                method :'direct_print_invoice',
		                args:[,order.name],
		                kwargs: {},
		            }).then(function(data){
		            	console.log('data',data)
		            	if(data){
		            		var invoice = {
                                           'name' : data['inv_name'],
                                           'origin' : data['inv_origin'],
                                           'date_invoice' : data['inv_date_invoice'],
                                           'date_due' : data['inv_date_due'],
                                           'number' : data['inv_number'],
                                           'amount_untaxed': data['amount_untaxed'],
                                           'amount_total':data['amount_total'],
                                           }
		            		var receipt = QWeb.render('POSDirectPrintInvoice',
			                    {   
			                       widget: self,
                                   pos: self.env.pos,
                                   order: order,
                                   receipt: order.export_for_printing(),
                                   orderlines: order.get_orderlines(),
                                   paymentlines: order.get_paymentlines(),
                                   customer : self.env.pos.attributes.selectedClient,
                                   invoice: invoice,
                                   invoice_data:data['invoice_data'],
                                   tax_data:data['tax_data'],
                                   inv_id:data['inv_id'],
                                   currency_id:data['currency_id']
			                    });


		            		if (self.env.pos.proxy.printer) {
				                const printResult = self.env.pos.proxy.printer.print_receipt(receipt);
				                if (printResult.successful) {
				                    return true;
				                } else {
				                    const { confirmed } = self.showPopup('ConfirmPopup', {
				                        title: printResult.message.title,
				                        body: 'Do you want to print using the web printer?',
				                    });
				                    if (confirmed) {
				                        try {
//				                            const printResult = await this.env.pos.proxy.printer.print_receipt(this.orderReceipt.el.outerHTML);
							                var window_open = window.open('', data['inv_name'], 'height=570, width=650, left=300, top=60');
				            				window_open.document.write('<html><body>'+receipt+'</body></html>');
				            				window_open.document.close();
				            				window_open.print();
//				    	                    window_open.close();

							                return true;
							            } catch (err) {
							                self.showPopup('ErrorPopup', {
							                    title: self.env._t('Printing is not supported on some browsers'),
							                    body: self.env._t(
							                        'Printing is not supported on some browsers due to no default printing protocol ' +
							                            'is available. It is possible to print your tickets by making use of an IoT Box.'
							                    ),
							                });
							                return false;
							            }
				                    }
				                    return false;
				                }
				            } else {
				                try {
					                var window_open = window.open('', data['inv_name'], 'height=570, width=650, left=300, top=60');
		            				window_open.document.write('<html><body>'+receipt+'</body></html>');
		            				window_open.document.close();
		            				window_open.print();
//		    	                    window_open.close();
					                return true;
					            } catch (err) {
					                self.showPopup('ErrorPopup', {
					                    title: self.env._t('Printing is not supported on some browsers'),
					                    body: self.env._t(
					                        'Printing is not supported on some browsers due to no default printing protocol ' +
					                            'is available. It is possible to print your tickets by making use of an IoT Box.'
					                    ),
					                });
					                return false;
					            }
				            }
	//	            		var do_action = self.chrome.do_action('point_of_sale.pos_invoice_report',{additional_context:{
	//                            active_ids: data.order_id,
	//                        }})
		            	}else{
		            		self.showPopup('ErrorPopup', {
			                    title: self.env._t('Printing is not supported on some browsers'),
			                    body: self.env._t('The order has been synchronized earlier. Please make the invoice from the backend for the order.'),
			                });
		            	}
		            });
				}else{
					self.showPopup('ErrorPopup', {
	                    title: self.env._t('Configuration'),
	                    body: self.env._t('Set Invoice Journal ID in POS Configuration.'),
	                });
				}
            }

	    };

	Registries.Component.extend(ReceiptScreen, PrintDirectInvoice);
	return ReceiptScreen;
});