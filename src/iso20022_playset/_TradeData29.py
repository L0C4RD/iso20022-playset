from . import base_types
from ._DetailedReportStatistics5 import DetailedReportStatistics5
from ._DetailedTransactionStatistics2Choice import DetailedTransactionStatistics2Choice
from ._SupplementaryData1 import SupplementaryData1

class TradeData29(base_types._BaseFieldType):

	__slots__ = ["_RptSttstcs", "_SplmtryData", "_TxSttstcs"]
	@property
	def RptSttstcs(self):
		return self._RptSttstcs

	@RptSttstcs.setter
	def RptSttstcs(self, value):
		self._RptSttstcs = value if type(value) != base_types.auto else self.make_default("RptSttstcs")

	@RptSttstcs.deleter
	def RptSttstcs(self):
		del self._RptSttstcs
		self._RptSttstcs = None

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
	def TxSttstcs(self):
		return self._TxSttstcs

	@TxSttstcs.setter
	def TxSttstcs(self, value):
		self._TxSttstcs = value if type(value) != base_types.auto else self.make_default("TxSttstcs")

	@TxSttstcs.deleter
	def TxSttstcs(self):
		del self._TxSttstcs
		self._TxSttstcs = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptSttstcs', type=DetailedReportStatistics5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSttstcs', type=DetailedTransactionStatistics2Choice, min=1, max=None, mutex_group=None, array=True),
	))

