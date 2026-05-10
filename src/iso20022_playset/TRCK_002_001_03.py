import base_types
import PaymentStatusTrackerReportV03

class TRCK_002_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PmtStsTrckrRpt"]
		@property
		def PmtStsTrckrRpt(self):
			return self._PmtStsTrckrRpt

		@PmtStsTrckrRpt.setter
		def PmtStsTrckrRpt(self, value):
			self._PmtStsTrckrRpt = value if type(value) != auto else self.make_default("PmtStsTrckrRpt")

		@PmtStsTrckrRpt.deleter
		def PmtStsTrckrRpt(self):
			del self._PmtStsTrckrRpt
			self._PmtStsTrckrRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtStsTrckrRpt', type=PaymentStatusTrackerReportV03, min=1, max=1, mutex_group=None, array=False),
		))

