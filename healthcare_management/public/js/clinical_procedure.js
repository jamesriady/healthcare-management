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