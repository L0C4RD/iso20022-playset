from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .PartyIdentification121Choice import PartyIdentification121Choice
from .TradeReportQuery18Choice import TradeReportQuery18Choice

class DerivativesTradeReportQueryV05(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TradQryData", "_RqstngAuthrty"]
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
	def TradQryData(self):
		return self._TradQryData

	@TradQryData.setter
	def TradQryData(self, value):
		self._TradQryData = value if type(value) != base_types.auto else self.make_default("TradQryData")

	@TradQryData.deleter
	def TradQryData(self):
		del self._TradQryData
		self._TradQryData = None

	@property
	def RqstngAuthrty(self):
		return self._RqstngAuthrty

	@RqstngAuthrty.setter
	def RqstngAuthrty(self, value):
		self._RqstngAuthrty = value if type(value) != base_types.auto else self.make_default("RqstngAuthrty")

	@RqstngAuthrty.deleter
	def RqstngAuthrty(self):
		del self._RqstngAuthrty
		self._RqstngAuthrty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradQryData', type=TradeReportQuery18Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqstngAuthrty', type=PartyIdentification121Choice, min=1, max=1, mutex_group=None, array=False),
	))

