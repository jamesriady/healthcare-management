from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
	custom_field = {
		"Clinical Procedure": [
			{
				"fetch_from": "patient.sex",
                "fieldname": "patient_sex",
                "fieldtype": "Link",
                "label": "Gender",
                "options": "Gender",
                "read_only": 1,
                "set_only_once": 1
			},
			{
				"fetch_from": "patient.patient_name",
                "fieldname": "patient_name",
                "fieldtype": "Data",
                "label": "Patient Name",
                "read_only": 1
            },
			{
				"fetch_from": "practitioner.practitioner_name",
                "fieldname": "practitioner_name",
                "fieldtype": "Data",
                "in_list_view": 1,
                "label": "Practitioner Name",
                "read_only": 1
            }
		]
	}
	
	create_custom_fields(custom_field, ignore_validate=True)
