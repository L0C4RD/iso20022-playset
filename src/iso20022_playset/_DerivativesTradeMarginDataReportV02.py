from . import base_types
from ._TradeReportHeader4 import TradeReportHeader4
from ._SupplementaryData1 import SupplementaryData1
from ._TradeData61Choice import TradeData61Choice

class DerivativesTradeMarginDataReportV02(base_types._BaseFieldType):

	__slots__ = ["_TradData", "_RptHdr", "_SplmtryData"]
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
		base_types.FieldEntry(name='RptHdr', type=TradeReportHeader4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradData', type=TradeData61Choice, min=1, max=1, mutex_group=None, array=False),
	))

