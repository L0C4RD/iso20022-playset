# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import DocumentGeneralInformation5
from . import DocumentIdentification22
from . import ExchangeRate1
from . import ISODate
from . import InterestPaymentDateRange1
from . import Max35Text
from . import ShipmentSchedule2Choice
from . import TradeParty6
from . import TrueFalseIndicator

class TradeContract4(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Attchmnt", "_Buyr", "_CtrctDocId", "_MtrtyDt", "_PmtSchdl", "_PrlngtnFlg", "_Sellr", "_ShipmntSchdl", "_StartDt", "_SttlmCcy", "_TradTpId", "_XchgRateInf"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if value is not None else base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = base_types.UninitialisedField(self, 'Attchmnt', DocumentGeneralInformation5, True)

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if value is not None else base_types.UninitialisedField(self, 'Buyr', TradeParty6, True)

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = base_types.UninitialisedField(self, 'Buyr', TradeParty6, True)

	@property
	def CtrctDocId(self):
		return self._CtrctDocId

	@CtrctDocId.setter
	def CtrctDocId(self, value):
		self._CtrctDocId = value if value is not None else base_types.UninitialisedField(self, 'CtrctDocId', DocumentIdentification22, False)

	@CtrctDocId.deleter
	def CtrctDocId(self):
		del self._CtrctDocId
		self._CtrctDocId = base_types.UninitialisedField(self, 'CtrctDocId', DocumentIdentification22, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODate, False)

	@property
	def PmtSchdl(self):
		return self._PmtSchdl

	@PmtSchdl.setter
	def PmtSchdl(self, value):
		self._PmtSchdl = value if value is not None else base_types.UninitialisedField(self, 'PmtSchdl', InterestPaymentDateRange1, False)

	@PmtSchdl.deleter
	def PmtSchdl(self):
		del self._PmtSchdl
		self._PmtSchdl = base_types.UninitialisedField(self, 'PmtSchdl', InterestPaymentDateRange1, False)

	@property
	def PrlngtnFlg(self):
		return self._PrlngtnFlg

	@PrlngtnFlg.setter
	def PrlngtnFlg(self, value):
		self._PrlngtnFlg = value if value is not None else base_types.UninitialisedField(self, 'PrlngtnFlg', TrueFalseIndicator, False)

	@PrlngtnFlg.deleter
	def PrlngtnFlg(self):
		del self._PrlngtnFlg
		self._PrlngtnFlg = base_types.UninitialisedField(self, 'PrlngtnFlg', TrueFalseIndicator, False)

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if value is not None else base_types.UninitialisedField(self, 'Sellr', TradeParty6, True)

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = base_types.UninitialisedField(self, 'Sellr', TradeParty6, True)

	@property
	def ShipmntSchdl(self):
		return self._ShipmntSchdl

	@ShipmntSchdl.setter
	def ShipmntSchdl(self, value):
		self._ShipmntSchdl = value if value is not None else base_types.UninitialisedField(self, 'ShipmntSchdl', ShipmentSchedule2Choice, False)

	@ShipmntSchdl.deleter
	def ShipmntSchdl(self):
		del self._ShipmntSchdl
		self._ShipmntSchdl = base_types.UninitialisedField(self, 'ShipmntSchdl', ShipmentSchedule2Choice, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if value is not None else base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = base_types.UninitialisedField(self, 'SttlmCcy', ActiveCurrencyCode, False)

	@property
	def TradTpId(self):
		return self._TradTpId

	@TradTpId.setter
	def TradTpId(self, value):
		self._TradTpId = value if value is not None else base_types.UninitialisedField(self, 'TradTpId', Max35Text, False)

	@TradTpId.deleter
	def TradTpId(self):
		del self._TradTpId
		self._TradTpId = base_types.UninitialisedField(self, 'TradTpId', Max35Text, False)

	@property
	def XchgRateInf(self):
		return self._XchgRateInf

	@XchgRateInf.setter
	def XchgRateInf(self, value):
		self._XchgRateInf = value if value is not None else base_types.UninitialisedField(self, 'XchgRateInf', ExchangeRate1, False)

	@XchgRateInf.deleter
	def XchgRateInf(self):
		del self._XchgRateInf
		self._XchgRateInf = base_types.UninitialisedField(self, 'XchgRateInf', ExchangeRate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Buyr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctDocId', type=DocumentIdentification22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtSchdl', type=InterestPaymentDateRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrlngtnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ShipmntSchdl', type=ShipmentSchedule2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateInf', type=ExchangeRate1, min=0, max=1, mutex_group=None, array=False),
	))