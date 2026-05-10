from . import base_types
from .SecuritiesFinancingReportingTransactionMarginDataReportV02 import SecuritiesFinancingReportingTransactionMarginDataReportV02

class AUTH_070_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesFincgRptgTxMrgnDataRpt"]
		@property
		def SctiesFincgRptgTxMrgnDataRpt(self):
			return self._SctiesFincgRptgTxMrgnDataRpt

		@SctiesFincgRptgTxMrgnDataRpt.setter
		def SctiesFincgRptgTxMrgnDataRpt(self, value):
			self._SctiesFincgRptgTxMrgnDataRpt = value if type(value) != base_types.auto else self.make_default("SctiesFincgRptgTxMrgnDataRpt")

		@SctiesFincgRptgTxMrgnDataRpt.deleter
		def SctiesFincgRptgTxMrgnDataRpt(self):
			del self._SctiesFincgRptgTxMrgnDataRpt
			self._SctiesFincgRptgTxMrgnDataRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesFincgRptgTxMrgnDataRpt', type=SecuritiesFinancingReportingTransactionMarginDataReportV02, min=1, max=1, mutex_group=None, array=False),
		))

