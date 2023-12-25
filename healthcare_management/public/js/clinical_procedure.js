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