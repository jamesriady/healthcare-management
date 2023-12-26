frappe.ui.form.on('Clinical Procedure', {
	onload: function(frm) {
		if (frm.is_new()) {
			frm.add_fetch('procedure_template', 'medical_department', 'medical_department');
			frm.set_value('start_time', null);

			if (frm.doc.practitioner) {
				frappe.call({
					'method': 'frappe.client.get',
					args: {
						doctype: 'Healthcare Practitioner',
						name: frm.doc.practitioner
					},
					callback: function (data) {
						frappe.model.set_value(frm.doctype,frm.docname, 'medical_department', data.message.department);
					}
				});
			}
		}
	},

	procedure_template: function(frm) {
		if (frm.doc.procedure_template) {
			frappe.call({
				'method': 'frappe.client.get',
				args: {
					doctype: 'Clinical Procedure Template',
					name: frm.doc.procedure_template
				},
				callback: function (data) {
					frm.set_value('medical_department', data.message.medical_department);
					frm.set_value('consume_stock', data.message.consume_stock);
					frm.events.set_warehouse(frm);
					frm.events.set_procedure_consumables(frm);
				}
			});
		}
	},
})

get_procedure_prescribed = function(frm){
	if (!frm.doc.patient) {
		frappe.msgprint(__("Please select Patient to get prescribed procedure"));
		return;
	}

	frappe.call({
		method:"healthcare_management.healthcare_management.custom_doctype.clinical_procedure.clinical_procedure.get_procedure_prescribed",
		args: {patient: frm.doc.patient},
		callback: function(r){
			show_procedure_templates(frm, r.message);
		}
	});
};

show_procedure_templates = function(frm, result){
	var d = new frappe.ui.Dialog({
		title: __("Prescribed Procedures"),
		fields: [{
				fieldtype: "HTML", fieldname: "procedure_template"
		}]
	});
	var html_field = d.fields_dict.procedure_template.$wrapper;
	html_field.empty();
	$.each(result, function(x, y){
		var row = $(repl(
			'<div class="col-xs-12 row" style="padding-top:12px;">\
				<div class="col-xs-3"> %(procedure_template)s </div>\
				<div class="col-xs-4">%(encounter)s</div>\
				<div class="col-xs-3"> %(date)s </div>\
				<div class="col-xs-1">\
				<a data-name="%(name)s" data-procedure-template="%(procedure_template)s"\
					data-encounter="%(encounter)s" data-practitioner="%(practitioner)s"\
					data-invoiced="%(invoiced)s" data-source="%(source)s"\
					href="#"><button class="btn btn-default btn-xs">Get</button></a>\
				</div>\
			</div><hr>',
			{ procedure_template: y[0], encounter: y[1], invoiced: y[2], practitioner: y[3], date: y[4],
				name: y[5]})
			).appendTo(html_field);
			row.find("a").click(function() {
			frappe.model.set_value(frm.doctype,frm.docname, 'procedure_template', $(this).attr("data-procedure-template"));
			frm.doc.service_request = $(this).attr('data-name');
			frm.doc.practitioner = $(this).attr("data-practitioner");
			frm.doc.invoiced = 0;
			if ($(this).attr('data-invoiced') === 1) {
				frm.doc.invoiced = 1;
			}
			frm.refresh_field("service_request");
			frm.refresh_field("practitioner");
			frm.refresh_field('invoiced');
			d.hide();
			return false;
		});
	});
	if(!result || result.length < 1){
		var msg = "There are no procedure prescribed for patient "+frm.doc.patient;
		$(repl('<div class="text-left">%(msg)s</div>', {msg: msg})).appendTo(html_field);
	}
	d.show();
};
