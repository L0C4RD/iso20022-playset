from . import base_types
from ._CustomerPaymentStatusReportV15 import CustomerPaymentStatusReportV15

class PAIN_002_001_15():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CstmrPmtStsRpt"]
		@property
		def CstmrPmtStsRpt(self):
			return self._CstmrPmtStsRpt

		@CstmrPmtStsRpt.setter
		def CstmrPmtStsRpt(self, value):
			self._CstmrPmtStsRpt = value if type(value) != base_types.auto else self.make_default("CstmrPmtStsRpt")

		@CstmrPmtStsRpt.deleter
		def CstmrPmtStsRpt(self):
			del self._CstmrPmtStsRpt
			self._CstmrPmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtStsRpt', type=CustomerPaymentStatusReportV15, min=1, max=1, mutex_group=None, array=False),
		))

