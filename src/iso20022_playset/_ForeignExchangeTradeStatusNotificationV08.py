from . import base_types
from ._RegulatoryReporting8 import RegulatoryReporting8
from ._SupplementaryData1 import SupplementaryData1
from ._TradeData15 import TradeData15

class ForeignExchangeTradeStatusNotificationV08(base_types._BaseFieldType):

	__slots__ = ["_TradData", "_SplmtryData", "_RgltryRptg"]
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
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if type(value) != base_types.auto else self.make_default("RgltryRptg")

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradData', type=TradeData15, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting8, min=0, max=1, mutex_group=None, array=False),
	))

