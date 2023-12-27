import frappe

from healthcare.healthcare.doctype.clinical_procedure.clinical_procedure import ClinicalProcedure

class KepinClinicalProcedure(ClinicalProcedure):
	def validate(self):
		super().validate()
		self.set_patient_age()

	def set_patient_age(self):
		patient = frappe.get_doc("Patient", self.patient)
		self.patient_age = patient.get_age()
		
@frappe.whitelist()
def get_procedure_prescribed(patient, encounter=False):
	hso = frappe.qb.DocType("Service Request")
	return (
		frappe.qb.from_(hso)
		.select(
			hso.template_dn, hso.order_group, hso.qty_invoiced, hso.practitioner, hso.order_date, hso.name
		)
		.where(hso.patient == patient)
		.where(hso.status != "Completed")
		.where(hso.template_dt == "Clinical Procedure Template")
		.orderby(hso.creation, order=frappe.qb.desc)
	).run()