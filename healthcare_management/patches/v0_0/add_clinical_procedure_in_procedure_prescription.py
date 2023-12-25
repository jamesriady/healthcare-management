from frappe.custom.doctype.custom_field.custom_field import create_custom_field

def execute():
    doctype = "Procedure Prescription"

    df = {
        "allow_on_submit": True,
        "fieldname": "clinical_procedure",
        "fieldtype": "Data",
        "label": "Clinical Procedure",
        "no_copy": True,
        "read_only": True,
        "insert_after": "service_request",
    }

    create_custom_field(doctype, df)