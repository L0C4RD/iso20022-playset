from . import base_types
from .Frequency1Code import Frequency1Code
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Max256Text import Max256Text
from .Rating1 import Rating1
from .TradeTransactionCondition2Code import TradeTransactionCondition2Code
from .ActiveCurrencyCode import ActiveCurrencyCode
from .ISOYearMonth import ISOYearMonth
from .FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from .ISODateTime import ISODateTime
from .AmountOrPercentageRange1 import AmountOrPercentageRange1
from .YesNoIndicator import YesNoIndicator
from .Number import Number
from .BICNonFIDec2014Identifier import BICNonFIDec2014Identifier
from .DateTimePeriod2 import DateTimePeriod2
from .Max35Text import Max35Text
from .PercentageRate import PercentageRate

class FinancialInstrumentStipulations4(base_types._BaseFieldType):

	__slots__ = ["_Hrcut", "_MaxSbstitn", "_PreFnddInd", "_CstmDt", "_AltrntvMinTaxInd", "_WhlPoolInd", "_Sctr", "_PutblInd", "_SbstitnFrqcy", "_MinIncrmt", "_EscrwdInd", "_LookBck", "_OverAlltmtRate", "_PricRg", "_IssrId", "_IsseDt", "_CpnRg", "_YldRg", "_PmtFrqcy", "_Pdctn", "_SbstitnLft", "_MinDnmtn", "_TxConds", "_Ccy", "_OverAlltmtAmt", "_ConvtblInd", "_MinQty", "_Ratg", "_AutoRinvstmt", "_RstrctdInd", "_PricSrc", "_AmtsblInd", "_IsseSz", "_CllblInd", "_Geogcs", "_InsrdInd", "_PerptlInd", "_XprtnDt", "_MtrtyDt", "_Purp", "_PricFrqcy"]
	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != base_types.auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	@property
	def MaxSbstitn(self):
		return self._MaxSbstitn

	@MaxSbstitn.setter
	def MaxSbstitn(self, value):
		self._MaxSbstitn = value if type(value) != base_types.auto else self.make_default("MaxSbstitn")

	@MaxSbstitn.deleter
	def MaxSbstitn(self):
		del self._MaxSbstitn
		self._MaxSbstitn = None

	@property
	def PreFnddInd(self):
		return self._PreFnddInd

	@PreFnddInd.setter
	def PreFnddInd(self, value):
		self._PreFnddInd = value if type(value) != base_types.auto else self.make_default("PreFnddInd")

	@PreFnddInd.deleter
	def PreFnddInd(self):
		del self._PreFnddInd
		self._PreFnddInd = None

	@property
	def CstmDt(self):
		return self._CstmDt

	@CstmDt.setter
	def CstmDt(self, value):
		self._CstmDt = value if type(value) != base_types.auto else self.make_default("CstmDt")

	@CstmDt.deleter
	def CstmDt(self):
		del self._CstmDt
		self._CstmDt = None

	@property
	def AltrntvMinTaxInd(self):
		return self._AltrntvMinTaxInd

	@AltrntvMinTaxInd.setter
	def AltrntvMinTaxInd(self, value):
		self._AltrntvMinTaxInd = value if type(value) != base_types.auto else self.make_default("AltrntvMinTaxInd")

	@AltrntvMinTaxInd.deleter
	def AltrntvMinTaxInd(self):
		del self._AltrntvMinTaxInd
		self._AltrntvMinTaxInd = None

	@property
	def WhlPoolInd(self):
		return self._WhlPoolInd

	@WhlPoolInd.setter
	def WhlPoolInd(self, value):
		self._WhlPoolInd = value if type(value) != base_types.auto else self.make_default("WhlPoolInd")

	@WhlPoolInd.deleter
	def WhlPoolInd(self):
		del self._WhlPoolInd
		self._WhlPoolInd = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != base_types.auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	@property
	def PutblInd(self):
		return self._PutblInd

	@PutblInd.setter
	def PutblInd(self, value):
		self._PutblInd = value if type(value) != base_types.auto else self.make_default("PutblInd")

	@PutblInd.deleter
	def PutblInd(self):
		del self._PutblInd
		self._PutblInd = None

	@property
	def SbstitnFrqcy(self):
		return self._SbstitnFrqcy

	@SbstitnFrqcy.setter
	def SbstitnFrqcy(self, value):
		self._SbstitnFrqcy = value if type(value) != base_types.auto else self.make_default("SbstitnFrqcy")

	@SbstitnFrqcy.deleter
	def SbstitnFrqcy(self):
		del self._SbstitnFrqcy
		self._SbstitnFrqcy = None

	@property
	def MinIncrmt(self):
		return self._MinIncrmt

	@MinIncrmt.setter
	def MinIncrmt(self, value):
		self._MinIncrmt = value if type(value) != base_types.auto else self.make_default("MinIncrmt")

	@MinIncrmt.deleter
	def MinIncrmt(self):
		del self._MinIncrmt
		self._MinIncrmt = None

	@property
	def EscrwdInd(self):
		return self._EscrwdInd

	@EscrwdInd.setter
	def EscrwdInd(self, value):
		self._EscrwdInd = value if type(value) != base_types.auto else self.make_default("EscrwdInd")

	@EscrwdInd.deleter
	def EscrwdInd(self):
		del self._EscrwdInd
		self._EscrwdInd = None

	@property
	def LookBck(self):
		return self._LookBck

	@LookBck.setter
	def LookBck(self, value):
		self._LookBck = value if type(value) != base_types.auto else self.make_default("LookBck")

	@LookBck.deleter
	def LookBck(self):
		del self._LookBck
		self._LookBck = None

	@property
	def OverAlltmtRate(self):
		return self._OverAlltmtRate

	@OverAlltmtRate.setter
	def OverAlltmtRate(self, value):
		self._OverAlltmtRate = value if type(value) != base_types.auto else self.make_default("OverAlltmtRate")

	@OverAlltmtRate.deleter
	def OverAlltmtRate(self):
		del self._OverAlltmtRate
		self._OverAlltmtRate = None

	@property
	def PricRg(self):
		return self._PricRg

	@PricRg.setter
	def PricRg(self, value):
		self._PricRg = value if type(value) != base_types.auto else self.make_default("PricRg")

	@PricRg.deleter
	def PricRg(self):
		del self._PricRg
		self._PricRg = None

	@property
	def IssrId(self):
		return self._IssrId

	@IssrId.setter
	def IssrId(self, value):
		self._IssrId = value if type(value) != base_types.auto else self.make_default("IssrId")

	@IssrId.deleter
	def IssrId(self):
		del self._IssrId
		self._IssrId = None

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if type(value) != base_types.auto else self.make_default("IsseDt")

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = None

	@property
	def CpnRg(self):
		return self._CpnRg

	@CpnRg.setter
	def CpnRg(self, value):
		self._CpnRg = value if type(value) != base_types.auto else self.make_default("CpnRg")

	@CpnRg.deleter
	def CpnRg(self):
		del self._CpnRg
		self._CpnRg = None

	@property
	def YldRg(self):
		return self._YldRg

	@YldRg.setter
	def YldRg(self, value):
		self._YldRg = value if type(value) != base_types.auto else self.make_default("YldRg")

	@YldRg.deleter
	def YldRg(self):
		del self._YldRg
		self._YldRg = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != base_types.auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def Pdctn(self):
		return self._Pdctn

	@Pdctn.setter
	def Pdctn(self, value):
		self._Pdctn = value if type(value) != base_types.auto else self.make_default("Pdctn")

	@Pdctn.deleter
	def Pdctn(self):
		del self._Pdctn
		self._Pdctn = None

	@property
	def SbstitnLft(self):
		return self._SbstitnLft

	@SbstitnLft.setter
	def SbstitnLft(self, value):
		self._SbstitnLft = value if type(value) != base_types.auto else self.make_default("SbstitnLft")

	@SbstitnLft.deleter
	def SbstitnLft(self):
		del self._SbstitnLft
		self._SbstitnLft = None

	@property
	def MinDnmtn(self):
		return self._MinDnmtn

	@MinDnmtn.setter
	def MinDnmtn(self, value):
		self._MinDnmtn = value if type(value) != base_types.auto else self.make_default("MinDnmtn")

	@MinDnmtn.deleter
	def MinDnmtn(self):
		del self._MinDnmtn
		self._MinDnmtn = None

	@property
	def TxConds(self):
		return self._TxConds

	@TxConds.setter
	def TxConds(self, value):
		self._TxConds = value if type(value) != base_types.auto else self.make_default("TxConds")

	@TxConds.deleter
	def TxConds(self):
		del self._TxConds
		self._TxConds = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def OverAlltmtAmt(self):
		return self._OverAlltmtAmt

	@OverAlltmtAmt.setter
	def OverAlltmtAmt(self, value):
		self._OverAlltmtAmt = value if type(value) != base_types.auto else self.make_default("OverAlltmtAmt")

	@OverAlltmtAmt.deleter
	def OverAlltmtAmt(self):
		del self._OverAlltmtAmt
		self._OverAlltmtAmt = None

	@property
	def ConvtblInd(self):
		return self._ConvtblInd

	@ConvtblInd.setter
	def ConvtblInd(self, value):
		self._ConvtblInd = value if type(value) != base_types.auto else self.make_default("ConvtblInd")

	@ConvtblInd.deleter
	def ConvtblInd(self):
		del self._ConvtblInd
		self._ConvtblInd = None

	@property
	def MinQty(self):
		return self._MinQty

	@MinQty.setter
	def MinQty(self, value):
		self._MinQty = value if type(value) != base_types.auto else self.make_default("MinQty")

	@MinQty.deleter
	def MinQty(self):
		del self._MinQty
		self._MinQty = None

	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if type(value) != base_types.auto else self.make_default("Ratg")

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = None

	@property
	def AutoRinvstmt(self):
		return self._AutoRinvstmt

	@AutoRinvstmt.setter
	def AutoRinvstmt(self, value):
		self._AutoRinvstmt = value if type(value) != base_types.auto else self.make_default("AutoRinvstmt")

	@AutoRinvstmt.deleter
	def AutoRinvstmt(self):
		del self._AutoRinvstmt
		self._AutoRinvstmt = None

	@property
	def RstrctdInd(self):
		return self._RstrctdInd

	@RstrctdInd.setter
	def RstrctdInd(self, value):
		self._RstrctdInd = value if type(value) != base_types.auto else self.make_default("RstrctdInd")

	@RstrctdInd.deleter
	def RstrctdInd(self):
		del self._RstrctdInd
		self._RstrctdInd = None

	@property
	def PricSrc(self):
		return self._PricSrc

	@PricSrc.setter
	def PricSrc(self, value):
		self._PricSrc = value if type(value) != base_types.auto else self.make_default("PricSrc")

	@PricSrc.deleter
	def PricSrc(self):
		del self._PricSrc
		self._PricSrc = None

	@property
	def AmtsblInd(self):
		return self._AmtsblInd

	@AmtsblInd.setter
	def AmtsblInd(self, value):
		self._AmtsblInd = value if type(value) != base_types.auto else self.make_default("AmtsblInd")

	@AmtsblInd.deleter
	def AmtsblInd(self):
		del self._AmtsblInd
		self._AmtsblInd = None

	@property
	def IsseSz(self):
		return self._IsseSz

	@IsseSz.setter
	def IsseSz(self, value):
		self._IsseSz = value if type(value) != base_types.auto else self.make_default("IsseSz")

	@IsseSz.deleter
	def IsseSz(self):
		del self._IsseSz
		self._IsseSz = None

	@property
	def CllblInd(self):
		return self._CllblInd

	@CllblInd.setter
	def CllblInd(self, value):
		self._CllblInd = value if type(value) != base_types.auto else self.make_default("CllblInd")

	@CllblInd.deleter
	def CllblInd(self):
		del self._CllblInd
		self._CllblInd = None

	@property
	def Geogcs(self):
		return self._Geogcs

	@Geogcs.setter
	def Geogcs(self, value):
		self._Geogcs = value if type(value) != base_types.auto else self.make_default("Geogcs")

	@Geogcs.deleter
	def Geogcs(self):
		del self._Geogcs
		self._Geogcs = None

	@property
	def InsrdInd(self):
		return self._InsrdInd

	@InsrdInd.setter
	def InsrdInd(self, value):
		self._InsrdInd = value if type(value) != base_types.auto else self.make_default("InsrdInd")

	@InsrdInd.deleter
	def InsrdInd(self):
		del self._InsrdInd
		self._InsrdInd = None

	@property
	def PerptlInd(self):
		return self._PerptlInd

	@PerptlInd.setter
	def PerptlInd(self, value):
		self._PerptlInd = value if type(value) != base_types.auto else self.make_default("PerptlInd")

	@PerptlInd.deleter
	def PerptlInd(self):
		del self._PerptlInd
		self._PerptlInd = None

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if type(value) != base_types.auto else self.make_default("XprtnDt")

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = None

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if type(value) != base_types.auto else self.make_default("MtrtyDt")

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != base_types.auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def PricFrqcy(self):
		return self._PricFrqcy

	@PricFrqcy.setter
	def PricFrqcy(self, value):
		self._PricFrqcy = value if type(value) != base_types.auto else self.make_default("PricFrqcy")

	@PricFrqcy.deleter
	def PricFrqcy(self):
		del self._PricFrqcy
		self._PricFrqcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSbstitn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreFnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmDt', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrntvMinTaxInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlPoolInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinIncrmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EscrwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LookBck', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrId', type=BICNonFIDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnLft', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinDnmtn', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxConds', type=TradeTransactionCondition2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ratg', type=Rating1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutoRinvstmt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtsblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseSz', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Geogcs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PerptlInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
	))

