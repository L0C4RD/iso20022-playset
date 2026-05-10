import base_types
import CustomerPaymentStatusReportV14

class PAIN_002_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CstmrPmtStsRpt"]
		@property
		def CstmrPmtStsRpt(self):
			return self._CstmrPmtStsRpt

		@CstmrPmtStsRpt.setter
		def CstmrPmtStsRpt(self, value):
			self._CstmrPmtStsRpt = value if type(value) != auto else self.make_default("CstmrPmtStsRpt")

		@CstmrPmtStsRpt.deleter
		def CstmrPmtStsRpt(self):
			del self._CstmrPmtStsRpt
			self._CstmrPmtStsRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtStsRpt', type=CustomerPaymentStatusReportV14, min=1, max=1, mutex_group=None, array=False),
		))

