import base_types
import AffirmStatus1Code
import ISODate
import TradingModeType1Code
import TradeConfirmationStatus1Code
import AdditionalInformation5
import MarketIdentification88
import MessageIdentification1
import Max35Text
import SupplementaryData1

class ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_TradDt", "_AffirmSts", "_TradId", "_MktId", "_TradgMd", "_ReqId", "_AdvcAckId", "_AddtlInf", "_ConfSts"]
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
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if type(value) != auto else self.make_default("AffirmSts")

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	@property
	def MktId(self):
		return self._MktId

	@MktId.setter
	def MktId(self, value):
		self._MktId = value if type(value) != auto else self.make_default("MktId")

	@MktId.deleter
	def MktId(self):
		del self._MktId
		self._MktId = None

	@property
	def TradgMd(self):
		return self._TradgMd

	@TradgMd.setter
	def TradgMd(self, value):
		self._TradgMd = value if type(value) != auto else self.make_default("TradgMd")

	@TradgMd.deleter
	def TradgMd(self):
		del self._TradgMd
		self._TradgMd = None

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if type(value) != auto else self.make_default("ReqId")

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = None

	@property
	def AdvcAckId(self):
		return self._AdvcAckId

	@AdvcAckId.setter
	def AdvcAckId(self, value):
		self._AdvcAckId = value if type(value) != auto else self.make_default("AdvcAckId")

	@AdvcAckId.deleter
	def AdvcAckId(self):
		del self._AdvcAckId
		self._AdvcAckId = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def ConfSts(self):
		return self._ConfSts

	@ConfSts.setter
	def ConfSts(self, value):
		self._ConfSts = value if type(value) != auto else self.make_default("ConfSts")

	@ConfSts.deleter
	def ConfSts(self):
		del self._ConfSts
		self._ConfSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktId', type=MarketIdentification88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMd', type=TradingModeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvcAckId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfSts', type=TradeConfirmationStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

