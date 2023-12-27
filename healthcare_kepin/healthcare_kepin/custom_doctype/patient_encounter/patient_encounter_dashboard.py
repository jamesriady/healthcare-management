from frappe import _

def get_dashboard_data(data):
	return {
		"fieldname": "encounter",
		"non_standard_fieldnames": {
			"Patient Medical Record": "reference_name",
			"Inpatient Medication Order": "patient_encounter",
			"Nursing Task": "reference_name",
			"Service Request": "order_group",
			"Medication Request": "order_group",
		},
		 "internal_links": {
            "Clinical Procedure": ["procedure_prescription", "clinical_procedure"],
        },
		"transactions": [
			{"label": _("Records"), "items": ["Vital Signs", "Patient Medical Record"]},
			{
				"label": _("Orders"),
				"items": [
					"Inpatient Medication Order",
					"Nursing Task",
					"Service Request",
					"Medication Request",
					"Clinical Procedure"
				],
			},
		],
		"disable_create_buttons": ["Inpatient Medication Order"],
	}
