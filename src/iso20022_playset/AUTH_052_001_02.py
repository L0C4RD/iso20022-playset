from . import base_types
from .SecuritiesFinancingReportingTransactionReportV02 import SecuritiesFinancingReportingTransactionReportV02

class AUTH_052_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgTxRpt"]
		@property
		def SctiesFincgRptgTxRpt(self):
			return self._SctiesFincgRptgTxRpt

		@SctiesFincgRptgTxRpt.setter
		def SctiesFincgRptgTxRpt(self, value):
			self._SctiesFincgRptgTxRpt = value if type(value) != auto else self.make_default("SctiesFincgRptgTxRpt")

		@SctiesFincgRptgTxRpt.deleter
		def SctiesFincgRptgTxRpt(self):
			del self._SctiesFincgRptgTxRpt
			self._SctiesFincgRptgTxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxRpt', type=SecuritiesFinancingReportingTransactionReportV02, min=1, max=1, mutex_group=None, array=False),
		))

