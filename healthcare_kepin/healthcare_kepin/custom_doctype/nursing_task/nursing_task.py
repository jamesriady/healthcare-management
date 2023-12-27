import frappe

import frappe
from frappe.utils import add_to_date, get_datetime, getdate, now_datetime

from healthcare.healthcare.doctype.nursing_task.nursing_task import NursingTask

class KepinNursingTask(NursingTask):
	def set_task_schedule(self):
		if not self.requested_start_time or (get_datetime(self.requested_start_time) < now_datetime()):
			self.requested_start_time = now_datetime()

		if not self.requested_end_time:
			if not self.duration:
				self.duration = frappe.db.get_value("Healthcare Activity", self.activity, "activity_duration")
			self.requested_end_time = add_to_date(self.requested_start_time, seconds=self.duration)

		# set date based on requested_start_time
		self.date = getdate(self.requested_start_time)