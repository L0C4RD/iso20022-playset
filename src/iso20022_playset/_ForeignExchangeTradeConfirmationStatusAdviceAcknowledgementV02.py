# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation5
from . import AffirmStatus1Code
from . import ISODate
from . import MarketIdentification88
from . import Max35Text
from . import MessageIdentification1
from . import SupplementaryData1
from . import TradeConfirmationStatus1Code
from . import TradingModeType1Code

class ForeignExchangeTradeConfirmationStatusAdviceAcknowledgementV02(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_AdvcAckId", "_AffirmSts", "_ConfSts", "_MktId", "_ReqId", "_SplmtryData", "_TradDt", "_TradId", "_TradgMd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation5, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation5, False)

	@property
	def AdvcAckId(self):
		return self._AdvcAckId

	@AdvcAckId.setter
	def AdvcAckId(self, value):
		self._AdvcAckId = value if value is not None else base_types.UninitialisedField(self, 'AdvcAckId', MessageIdentification1, False)

	@AdvcAckId.deleter
	def AdvcAckId(self):
		del self._AdvcAckId
		self._AdvcAckId = base_types.UninitialisedField(self, 'AdvcAckId', MessageIdentification1, False)

	@property
	def AffirmSts(self):
		return self._AffirmSts

	@AffirmSts.setter
	def AffirmSts(self, value):
		self._AffirmSts = value if value is not None else base_types.UninitialisedField(self, 'AffirmSts', AffirmStatus1Code, False)

	@AffirmSts.deleter
	def AffirmSts(self):
		del self._AffirmSts
		self._AffirmSts = base_types.UninitialisedField(self, 'AffirmSts', AffirmStatus1Code, False)

	@property
	def ConfSts(self):
		return self._ConfSts

	@ConfSts.setter
	def ConfSts(self, value):
		self._ConfSts = value if value is not None else base_types.UninitialisedField(self, 'ConfSts', TradeConfirmationStatus1Code, False)

	@ConfSts.deleter
	def ConfSts(self):
		del self._ConfSts
		self._ConfSts = base_types.UninitialisedField(self, 'ConfSts', TradeConfirmationStatus1Code, False)

	@property
	def MktId(self):
		return self._MktId

	@MktId.setter
	def MktId(self, value):
		self._MktId = value if value is not None else base_types.UninitialisedField(self, 'MktId', MarketIdentification88, False)

	@MktId.deleter
	def MktId(self):
		del self._MktId
		self._MktId = base_types.UninitialisedField(self, 'MktId', MarketIdentification88, False)

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if value is not None else base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if value is not None else base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = base_types.UninitialisedField(self, 'TradId', Max35Text, False)

	@property
	def TradgMd(self):
		return self._TradgMd

	@TradgMd.setter
	def TradgMd(self, value):
		self._TradgMd = value if value is not None else base_types.UninitialisedField(self, 'TradgMd', TradingModeType1Code, False)

	@TradgMd.deleter
	def TradgMd(self):
		del self._TradgMd
		self._TradgMd = base_types.UninitialisedField(self, 'TradgMd', TradingModeType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AdvcAckId', type=MessageIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AffirmSts', type=AffirmStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConfSts', type=TradeConfirmationStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktId', type=MarketIdentification88, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgMd', type=TradingModeType1Code, min=1, max=1, mutex_group=None, array=False),
	))