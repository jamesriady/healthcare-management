frappe.ui.form.on('Procedure Prescription', {
	procedure: function(frm, cdt, cdn){
		let child = locals[cdt][cdn];
		if (!child.practitioner) {
			frappe.model.set_value(cdt, cdn, 'practitioner', frm.doc.practitioner);
		}
		if (!child.date) {
			frappe.model.set_value(cdt, cdn, 'date', frappe.datetime.nowdate());
		}
	},
});