from . import base_types
import DocumentGeneralInformation5
import ISODate
import TradeParty6
import ShipmentSchedule2Choice
import ExchangeRate1
import Max35Text
import ActiveCurrencyAndAmount
import ActiveCurrencyCode
import InterestPaymentDateRange1
import TrueFalseIndicator
import DocumentIdentification22

class TradeContract4(base_types._BaseFieldType):

	__slots__ = ["_Attchmnt", "_PmtSchdl", "_Buyr", "_MtrtyDt", "_CtrctDocId", "_PrlngtnFlg", "_Amt", "_ShipmntSchdl", "_Sellr", "_TradTpId", "_SttlmCcy", "_XchgRateInf", "_StartDt"]
	@property
	def Attchmnt(self):
		return self._Attchmnt

	@Attchmnt.setter
	def Attchmnt(self, value):
		self._Attchmnt = value if type(value) != auto else self.make_default("Attchmnt")

	@Attchmnt.deleter
	def Attchmnt(self):
		del self._Attchmnt
		self._Attchmnt = None

	@property
	def PmtSchdl(self):
		return self._PmtSchdl

	@PmtSchdl.setter
	def PmtSchdl(self, value):
		self._PmtSchdl = value if type(value) != auto else self.make_default("PmtSchdl")

	@PmtSchdl.deleter
	def PmtSchdl(self):
		del self._PmtSchdl
		self._PmtSchdl = None

	@property
	def Buyr(self):
		return self._Buyr

	@Buyr.setter
	def Buyr(self, value):
		self._Buyr = value if type(value) != auto else self.make_default("Buyr")

	@Buyr.deleter
	def Buyr(self):
		del self._Buyr
		self._Buyr = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def CtrctDocId(self):
		return self._CtrctDocId

	@CtrctDocId.setter
	def CtrctDocId(self, value):
		self._CtrctDocId = value if type(value) != auto else self.make_default("CtrctDocId")

	@CtrctDocId.deleter
	def CtrctDocId(self):
		del self._CtrctDocId
		self._CtrctDocId = None

	@property
	def PrlngtnFlg(self):
		return self._PrlngtnFlg

	@PrlngtnFlg.setter
	def PrlngtnFlg(self, value):
		self._PrlngtnFlg = value if type(value) != auto else self.make_default("PrlngtnFlg")

	@PrlngtnFlg.deleter
	def PrlngtnFlg(self):
		del self._PrlngtnFlg
		self._PrlngtnFlg = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def ShipmntSchdl(self):
		return self._ShipmntSchdl

	@ShipmntSchdl.setter
	def ShipmntSchdl(self, value):
		self._ShipmntSchdl = value if type(value) != auto else self.make_default("ShipmntSchdl")

	@ShipmntSchdl.deleter
	def ShipmntSchdl(self):
		del self._ShipmntSchdl
		self._ShipmntSchdl = None

	@property
	def Sellr(self):
		return self._Sellr

	@Sellr.setter
	def Sellr(self, value):
		self._Sellr = value if type(value) != auto else self.make_default("Sellr")

	@Sellr.deleter
	def Sellr(self):
		del self._Sellr
		self._Sellr = None

	@property
	def TradTpId(self):
		return self._TradTpId

	@TradTpId.setter
	def TradTpId(self, value):
		self._TradTpId = value if type(value) != auto else self.make_default("TradTpId")

	@TradTpId.deleter
	def TradTpId(self):
		del self._TradTpId
		self._TradTpId = None

	@property
	def SttlmCcy(self):
		return self._SttlmCcy

	@SttlmCcy.setter
	def SttlmCcy(self, value):
		self._SttlmCcy = value if type(value) != auto else self.make_default("SttlmCcy")

	@SttlmCcy.deleter
	def SttlmCcy(self):
		del self._SttlmCcy
		self._SttlmCcy = None

	@property
	def XchgRateInf(self):
		return self._XchgRateInf

	@XchgRateInf.setter
	def XchgRateInf(self, value):
		self._XchgRateInf = value if type(value) != auto else self.make_default("XchgRateInf")

	@XchgRateInf.deleter
	def XchgRateInf(self):
		del self._XchgRateInf
		self._XchgRateInf = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attchmnt', type=DocumentGeneralInformation5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtSchdl', type=InterestPaymentDateRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Buyr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctDocId', type=DocumentIdentification22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrlngtnFlg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShipmntSchdl', type=ShipmentSchedule2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sellr', type=TradeParty6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TradTpId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateInf', type=ExchangeRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

