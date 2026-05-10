from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .TradeData35Choice import TradeData35Choice

class SecuritiesFinancingReportingTransactionStatusAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TxRptStsAndRsn"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TxRptStsAndRsn(self):
		return self._TxRptStsAndRsn

	@TxRptStsAndRsn.setter
	def TxRptStsAndRsn(self, value):
		self._TxRptStsAndRsn = value if type(value) != base_types.auto else self.make_default("TxRptStsAndRsn")

	@TxRptStsAndRsn.deleter
	def TxRptStsAndRsn(self):
		del self._TxRptStsAndRsn
		self._TxRptStsAndRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxRptStsAndRsn', type=TradeData35Choice, min=1, max=None, mutex_group=None, array=True),
	))

