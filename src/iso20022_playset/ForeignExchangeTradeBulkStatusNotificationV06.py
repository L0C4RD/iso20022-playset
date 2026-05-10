from . import base_types
import TradeData45
import SupplementaryData1
import Pagination1
import TradeDataReport2

class ForeignExchangeTradeBulkStatusNotificationV06(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_StsDtls", "_TradDataRpt", "_MsgPgntn"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def StsDtls(self):
		return self._StsDtls

	@StsDtls.setter
	def StsDtls(self, value):
		self._StsDtls = value if type(value) != auto else self.make_default("StsDtls")

	@StsDtls.deleter
	def StsDtls(self):
		del self._StsDtls
		self._StsDtls = None

	@property
	def TradDataRpt(self):
		return self._TradDataRpt

	@TradDataRpt.setter
	def TradDataRpt(self, value):
		self._TradDataRpt = value if type(value) != auto else self.make_default("TradDataRpt")

	@TradDataRpt.deleter
	def TradDataRpt(self):
		del self._TradDataRpt
		self._TradDataRpt = None

	@property
	def MsgPgntn(self):
		return self._MsgPgntn

	@MsgPgntn.setter
	def MsgPgntn(self, value):
		self._MsgPgntn = value if type(value) != auto else self.make_default("MsgPgntn")

	@MsgPgntn.deleter
	def MsgPgntn(self):
		del self._MsgPgntn
		self._MsgPgntn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsDtls', type=TradeData45, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDataRpt', type=TradeDataReport2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgPgntn', type=Pagination1, min=0, max=1, mutex_group=None, array=False),
	))

