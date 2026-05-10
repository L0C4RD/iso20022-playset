from . import base_types
from ._Side1Code import Side1Code
from ._MarketIdentification84 import MarketIdentification84
from ._SafekeepingPlaceFormat43Choice import SafekeepingPlaceFormat43Choice
from ._Price14 import Price14
from ._PartyIdentification253Choice import PartyIdentification253Choice
from ._ISODate import ISODate
from ._CurrencyCode import CurrencyCode
from ._DateFormat66Choice import DateFormat66Choice
from ._AmountAndDirection21 import AmountAndDirection21
from ._MarketIdentification85 import MarketIdentification85
from ._UTIIdentifier import UTIIdentifier
from ._TradingCapacity5Code import TradingCapacity5Code
from ._TradePosting1Code import TradePosting1Code
from ._PartyIdentificationAndAccount230 import PartyIdentificationAndAccount230
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._Max35Text import Max35Text
from ._SecuritiesAccount19 import SecuritiesAccount19
from ._YesNoIndicator import YesNoIndicator
from ._TradeType1Code import TradeType1Code
from ._ISODateTime import ISODateTime

class TradeLeg13(base_types._BaseFieldType):

	__slots__ = ["_SfkpgAcct", "_DealPric", "_TxDtAndTm", "_AllcnId", "_TradgCpcty", "_OrdrId", "_PlcOfTrad", "_PlcOfListg", "_GrssAmt", "_TradRegnOrgn", "_TradTp", "_TradgPty", "_SttlmDt", "_Brkr", "_TradPstngCd", "_TradDt", "_TradgCcy", "_TradExctnId", "_BuySellInd", "_SfkpgPlc", "_DerivRltdTrad", "_UnqTxIdr", "_TradId", "_TradQty", "_TradLegId", "_TradgPtyAcct"]
	@property
	def SfkpgAcct(self):
		return self._SfkpgAcct

	@SfkpgAcct.setter
	def SfkpgAcct(self, value):
		self._SfkpgAcct = value if type(value) != base_types.auto else self.make_default("SfkpgAcct")

	@SfkpgAcct.deleter
	def SfkpgAcct(self):
		del self._SfkpgAcct
		self._SfkpgAcct = None

	@property
	def DealPric(self):
		return self._DealPric

	@DealPric.setter
	def DealPric(self, value):
		self._DealPric = value if type(value) != base_types.auto else self.make_default("DealPric")

	@DealPric.deleter
	def DealPric(self):
		del self._DealPric
		self._DealPric = None

	@property
	def TxDtAndTm(self):
		return self._TxDtAndTm

	@TxDtAndTm.setter
	def TxDtAndTm(self, value):
		self._TxDtAndTm = value if type(value) != base_types.auto else self.make_default("TxDtAndTm")

	@TxDtAndTm.deleter
	def TxDtAndTm(self):
		del self._TxDtAndTm
		self._TxDtAndTm = None

	@property
	def AllcnId(self):
		return self._AllcnId

	@AllcnId.setter
	def AllcnId(self, value):
		self._AllcnId = value if type(value) != base_types.auto else self.make_default("AllcnId")

	@AllcnId.deleter
	def AllcnId(self):
		del self._AllcnId
		self._AllcnId = None

	@property
	def TradgCpcty(self):
		return self._TradgCpcty

	@TradgCpcty.setter
	def TradgCpcty(self, value):
		self._TradgCpcty = value if type(value) != base_types.auto else self.make_default("TradgCpcty")

	@TradgCpcty.deleter
	def TradgCpcty(self):
		del self._TradgCpcty
		self._TradgCpcty = None

	@property
	def OrdrId(self):
		return self._OrdrId

	@OrdrId.setter
	def OrdrId(self, value):
		self._OrdrId = value if type(value) != base_types.auto else self.make_default("OrdrId")

	@OrdrId.deleter
	def OrdrId(self):
		del self._OrdrId
		self._OrdrId = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != base_types.auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def PlcOfListg(self):
		return self._PlcOfListg

	@PlcOfListg.setter
	def PlcOfListg(self, value):
		self._PlcOfListg = value if type(value) != base_types.auto else self.make_default("PlcOfListg")

	@PlcOfListg.deleter
	def PlcOfListg(self):
		del self._PlcOfListg
		self._PlcOfListg = None

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != base_types.auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

	@property
	def TradRegnOrgn(self):
		return self._TradRegnOrgn

	@TradRegnOrgn.setter
	def TradRegnOrgn(self, value):
		self._TradRegnOrgn = value if type(value) != base_types.auto else self.make_default("TradRegnOrgn")

	@TradRegnOrgn.deleter
	def TradRegnOrgn(self):
		del self._TradRegnOrgn
		self._TradRegnOrgn = None

	@property
	def TradTp(self):
		return self._TradTp

	@TradTp.setter
	def TradTp(self, value):
		self._TradTp = value if type(value) != base_types.auto else self.make_default("TradTp")

	@TradTp.deleter
	def TradTp(self):
		del self._TradTp
		self._TradTp = None

	@property
	def TradgPty(self):
		return self._TradgPty

	@TradgPty.setter
	def TradgPty(self, value):
		self._TradgPty = value if type(value) != base_types.auto else self.make_default("TradgPty")

	@TradgPty.deleter
	def TradgPty(self):
		del self._TradgPty
		self._TradgPty = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != base_types.auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

	@property
	def Brkr(self):
		return self._Brkr

	@Brkr.setter
	def Brkr(self, value):
		self._Brkr = value if type(value) != base_types.auto else self.make_default("Brkr")

	@Brkr.deleter
	def Brkr(self):
		del self._Brkr
		self._Brkr = None

	@property
	def TradPstngCd(self):
		return self._TradPstngCd

	@TradPstngCd.setter
	def TradPstngCd(self, value):
		self._TradPstngCd = value if type(value) != base_types.auto else self.make_default("TradPstngCd")

	@TradPstngCd.deleter
	def TradPstngCd(self):
		del self._TradPstngCd
		self._TradPstngCd = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def TradgCcy(self):
		return self._TradgCcy

	@TradgCcy.setter
	def TradgCcy(self, value):
		self._TradgCcy = value if type(value) != base_types.auto else self.make_default("TradgCcy")

	@TradgCcy.deleter
	def TradgCcy(self):
		del self._TradgCcy
		self._TradgCcy = None

	@property
	def TradExctnId(self):
		return self._TradExctnId

	@TradExctnId.setter
	def TradExctnId(self, value):
		self._TradExctnId = value if type(value) != base_types.auto else self.make_default("TradExctnId")

	@TradExctnId.deleter
	def TradExctnId(self):
		del self._TradExctnId
		self._TradExctnId = None

	@property
	def BuySellInd(self):
		return self._BuySellInd

	@BuySellInd.setter
	def BuySellInd(self, value):
		self._BuySellInd = value if type(value) != base_types.auto else self.make_default("BuySellInd")

	@BuySellInd.deleter
	def BuySellInd(self):
		del self._BuySellInd
		self._BuySellInd = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != base_types.auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def DerivRltdTrad(self):
		return self._DerivRltdTrad

	@DerivRltdTrad.setter
	def DerivRltdTrad(self, value):
		self._DerivRltdTrad = value if type(value) != base_types.auto else self.make_default("DerivRltdTrad")

	@DerivRltdTrad.deleter
	def DerivRltdTrad(self):
		del self._DerivRltdTrad
		self._DerivRltdTrad = None

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if type(value) != base_types.auto else self.make_default("UnqTxIdr")

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = None

	@property
	def TradId(self):
		return self._TradId

	@TradId.setter
	def TradId(self, value):
		self._TradId = value if type(value) != base_types.auto else self.make_default("TradId")

	@TradId.deleter
	def TradId(self):
		del self._TradId
		self._TradId = None

	@property
	def TradQty(self):
		return self._TradQty

	@TradQty.setter
	def TradQty(self, value):
		self._TradQty = value if type(value) != base_types.auto else self.make_default("TradQty")

	@TradQty.deleter
	def TradQty(self):
		del self._TradQty
		self._TradQty = None

	@property
	def TradLegId(self):
		return self._TradLegId

	@TradLegId.setter
	def TradLegId(self, value):
		self._TradLegId = value if type(value) != base_types.auto else self.make_default("TradLegId")

	@TradLegId.deleter
	def TradLegId(self):
		del self._TradLegId
		self._TradLegId = None

	@property
	def TradgPtyAcct(self):
		return self._TradgPtyAcct

	@TradgPtyAcct.setter
	def TradgPtyAcct(self, value):
		self._TradgPtyAcct = value if type(value) != base_types.auto else self.make_default("TradgPtyAcct")

	@TradgPtyAcct.deleter
	def TradgPtyAcct(self):
		del self._TradgPtyAcct
		self._TradgPtyAcct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SfkpgAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealPric', type=Price14, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtAndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllcnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCpcty', type=TradingCapacity5Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=MarketIdentification84, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfListg', type=MarketIdentification85, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=AmountAndDirection21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRegnOrgn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradTp', type=TradeType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPty', type=PartyIdentification253Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=DateFormat66Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brkr', type=PartyIdentificationAndAccount230, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradPstngCd', type=TradePosting1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgCcy', type=CurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradExctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuySellInd', type=Side1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormat43Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DerivRltdTrad', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradLegId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradgPtyAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
	))

