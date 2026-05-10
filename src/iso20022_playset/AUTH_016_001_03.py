from . import base_types
from .FinancialInstrumentReportingTransactionReportV03 import FinancialInstrumentReportingTransactionReportV03

class AUTH_016_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FinInstrmRptgTxRpt"]
		@property
		def FinInstrmRptgTxRpt(self):
			return self._FinInstrmRptgTxRpt

		@FinInstrmRptgTxRpt.setter
		def FinInstrmRptgTxRpt(self, value):
			self._FinInstrmRptgTxRpt = value if type(value) != auto else self.make_default("FinInstrmRptgTxRpt")

		@FinInstrmRptgTxRpt.deleter
		def FinInstrmRptgTxRpt(self):
			del self._FinInstrmRptgTxRpt
			self._FinInstrmRptgTxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FinInstrmRptgTxRpt', type=FinancialInstrumentReportingTransactionReportV03, min=1, max=1, mutex_group=None, array=False),
		))

