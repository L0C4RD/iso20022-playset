from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .TradeData62Choice import TradeData62Choice
from .TradeReportHeader4 import TradeReportHeader4

class DerivativesTradeMarginDataTransactionStateReportV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_RptHdr", "_TradData"]
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
	def RptHdr(self):
		return self._RptHdr

	@RptHdr.setter
	def RptHdr(self, value):
		self._RptHdr = value if type(value) != base_types.auto else self.make_default("RptHdr")

	@RptHdr.deleter
	def RptHdr(self):
		del self._RptHdr
		self._RptHdr = None

	@property
	def TradData(self):
		return self._TradData

	@TradData.setter
	def TradData(self, value):
		self._TradData = value if type(value) != base_types.auto else self.make_default("TradData")

	@TradData.deleter
	def TradData(self):
		del self._TradData
		self._TradData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptHdr', type=TradeReportHeader4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradData', type=TradeData62Choice, min=1, max=1, mutex_group=None, array=False),
	))

