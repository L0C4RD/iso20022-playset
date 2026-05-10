from . import base_types
import FIToFIPaymentStatusReportV12

class PACS_002_001_12():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FIToFIPmtStsRpt"]
		@property
		def FIToFIPmtStsRpt(self):
			return self._FIToFIPmtStsRpt

		@FIToFIPmtStsRpt.setter
		def FIToFIPmtStsRpt(self, value):
			self._FIToFIPmtStsRpt = value if type(value) != auto else self.make_default("FIToFIPmtStsRpt")

		@FIToFIPmtStsRpt.deleter
		def FIToFIPmtStsRpt(self):
			del self._FIToFIPmtStsRpt
			self._FIToFIPmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtStsRpt', type=FIToFIPaymentStatusReportV12, min=1, max=1, mutex_group=None, array=False),
		))

