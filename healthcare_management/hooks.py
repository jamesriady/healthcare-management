app_name = "healthcare_management"
app_title = "Healthcare Management"
app_publisher = "James Riady"
app_description = "Healthcare Mangement System"
app_email = "jamesriady1998@gmail.com"
app_license = "\'healthcare_management\' created at /home/frappe/frappe-bench/apps/healthcare_management"
required_apps = ["healthcare"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/healthcare_management/css/healthcare_management.css"
# app_include_js = "/assets/healthcare_management/js/healthcare_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/healthcare_management/css/healthcare_management.css"
# web_include_js = "/assets/healthcare_management/js/healthcare_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "healthcare_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "healthcare_management.utils.jinja_methods",
#	"filters": "healthcare_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "healthcare_management.install.before_install"
# after_install = "healthcare_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "healthcare_management.uninstall.before_uninstall"
# after_uninstall = "healthcare_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "healthcare_management.utils.before_app_install"
# after_app_install = "healthcare_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "healthcare_management.utils.before_app_uninstall"
# after_app_uninstall = "healthcare_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "healthcare_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Sales Invoice": "healthcare_management.healthcare_management.custom_doctype.sales_invoice.sales_invoice.HealthcareSalesInvoice",
	"Clinical Procedure": "healthcare_management.healthcare_management.custom_doctype.clinical_procedure.clinical_procedure.HealthcareClinicalProcedure",
	"Patient Encounter": "healthcare_management.healthcare_management.custom_doctype.patient_encounter.patient_encounter.HealthcarePatientEncounter",
	"Nursing Task": "healthcare_management.healthcare_management.custom_doctype.nursing_task.nursing_task.HealthcareNursingTask",
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"healthcare_management.tasks.all"
#	],
#	"daily": [
#		"healthcare_management.tasks.daily"
#	],
#	"hourly": [
#		"healthcare_management.tasks.hourly"
#	],
#	"weekly": [
#		"healthcare_management.tasks.weekly"
#	],
#	"monthly": [
#		"healthcare_management.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "healthcare_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "healthcare_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
override_doctype_dashboards = {
	"Patient Encounter": "healthcare_management.healthcare_management.custom_doctype.patient_encounter.patient_encounter_dashboard.get_dashboard_data",
}

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["healthcare_management.utils.before_request"]
# after_request = ["healthcare_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["healthcare_management.utils.before_job"]
# after_job = ["healthcare_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"healthcare_management.auth.validate"
# ]
