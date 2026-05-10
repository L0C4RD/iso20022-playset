from . import base_types
from .PaymentStatusCustomerTrackerReportV03 import PaymentStatusCustomerTrackerReportV03

class TRCK_004_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PmtStsCstmrTrckrRpt"]
		@property
		def PmtStsCstmrTrckrRpt(self):
			return self._PmtStsCstmrTrckrRpt

		@PmtStsCstmrTrckrRpt.setter
		def PmtStsCstmrTrckrRpt(self, value):
			self._PmtStsCstmrTrckrRpt = value if type(value) != auto else self.make_default("PmtStsCstmrTrckrRpt")

		@PmtStsCstmrTrckrRpt.deleter
		def PmtStsCstmrTrckrRpt(self):
			del self._PmtStsCstmrTrckrRpt
			self._PmtStsCstmrTrckrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsCstmrTrckrRpt', type=PaymentStatusCustomerTrackerReportV03, min=1, max=1, mutex_group=None, array=False),
		))

