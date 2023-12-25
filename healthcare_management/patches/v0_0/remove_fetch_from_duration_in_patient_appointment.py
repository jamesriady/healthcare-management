from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
	custom_field = {
		"Patient Appointment": [
			{
				"fieldname": "duration",
				"fieldtype": "Int",
				"in_filter": 1,
				"label": "Duration (In Minutes)",
				"set_only_once": 1
			}
		]
	}
	
	create_custom_fields(custom_field, ignore_validate=True)
