frappe.ui.form.on('Patient Appointment', {
    appointment_type: function(frm) {
		if (frm.doc.appointment_type) {
			if (frm.doc.appointment_for && frm.doc[frappe.scrub(frm.doc.appointment_for)]) {
				frm.events.set_payment_details(frm);
			}

			frm.events.set_appointment_type_fields(frm);
		}
	},

	set_appointment_type_fields: function(frm) {
		frappe.call({
			method: 'frappe.client.get',
			args: {
				doctype: 'Appointment Type',
				name: frm.doc.appointment_type
			},
			callback: function(data) {
				let values = {
					'duration': data.message.default_duration
				};
				frm.set_value(values);
			}
		});
	},
})