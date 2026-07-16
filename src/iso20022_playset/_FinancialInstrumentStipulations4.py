# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import AmountOrPercentageRange1
from . import BICNonFIDec2014Identifier
from . import DateTimePeriod2
from . import FinancialInstrumentQuantity1Choice
from . import Frequency1Code
from . import ISODateTime
from . import ISOYearMonth
from . import Max256Text
from . import Max35Text
from . import Number
from . import PercentageRate
from . import Rating1
from . import TradeTransactionCondition2Code
from . import YesNoIndicator

class FinancialInstrumentStipulations4(base_types._BaseFieldType):

	__slots__ = ["_AltrntvMinTaxInd", "_AmtsblInd", "_AutoRinvstmt", "_Ccy", "_CllblInd", "_ConvtblInd", "_CpnRg", "_CstmDt", "_EscrwdInd", "_Geogcs", "_Hrcut", "_InsrdInd", "_IsseDt", "_IsseSz", "_IssrId", "_LookBck", "_MaxSbstitn", "_MinDnmtn", "_MinIncrmt", "_MinQty", "_MtrtyDt", "_OverAlltmtAmt", "_OverAlltmtRate", "_Pdctn", "_PerptlInd", "_PmtFrqcy", "_PreFnddInd", "_PricFrqcy", "_PricRg", "_PricSrc", "_Purp", "_PutblInd", "_Ratg", "_RstrctdInd", "_SbstitnFrqcy", "_SbstitnLft", "_Sctr", "_TxConds", "_WhlPoolInd", "_XprtnDt", "_YldRg"]
	@property
	def AltrntvMinTaxInd(self):
		return self._AltrntvMinTaxInd

	@AltrntvMinTaxInd.setter
	def AltrntvMinTaxInd(self, value):
		self._AltrntvMinTaxInd = value if value is not None else base_types.UninitialisedField(self, 'AltrntvMinTaxInd', YesNoIndicator, False)

	@AltrntvMinTaxInd.deleter
	def AltrntvMinTaxInd(self):
		del self._AltrntvMinTaxInd
		self._AltrntvMinTaxInd = base_types.UninitialisedField(self, 'AltrntvMinTaxInd', YesNoIndicator, False)

	@property
	def AmtsblInd(self):
		return self._AmtsblInd

	@AmtsblInd.setter
	def AmtsblInd(self, value):
		self._AmtsblInd = value if value is not None else base_types.UninitialisedField(self, 'AmtsblInd', YesNoIndicator, False)

	@AmtsblInd.deleter
	def AmtsblInd(self):
		del self._AmtsblInd
		self._AmtsblInd = base_types.UninitialisedField(self, 'AmtsblInd', YesNoIndicator, False)

	@property
	def AutoRinvstmt(self):
		return self._AutoRinvstmt

	@AutoRinvstmt.setter
	def AutoRinvstmt(self, value):
		self._AutoRinvstmt = value if value is not None else base_types.UninitialisedField(self, 'AutoRinvstmt', PercentageRate, False)

	@AutoRinvstmt.deleter
	def AutoRinvstmt(self):
		del self._AutoRinvstmt
		self._AutoRinvstmt = base_types.UninitialisedField(self, 'AutoRinvstmt', PercentageRate, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveCurrencyCode, False)

	@property
	def CllblInd(self):
		return self._CllblInd

	@CllblInd.setter
	def CllblInd(self, value):
		self._CllblInd = value if value is not None else base_types.UninitialisedField(self, 'CllblInd', YesNoIndicator, False)

	@CllblInd.deleter
	def CllblInd(self):
		del self._CllblInd
		self._CllblInd = base_types.UninitialisedField(self, 'CllblInd', YesNoIndicator, False)

	@property
	def ConvtblInd(self):
		return self._ConvtblInd

	@ConvtblInd.setter
	def ConvtblInd(self, value):
		self._ConvtblInd = value if value is not None else base_types.UninitialisedField(self, 'ConvtblInd', YesNoIndicator, False)

	@ConvtblInd.deleter
	def ConvtblInd(self):
		del self._ConvtblInd
		self._ConvtblInd = base_types.UninitialisedField(self, 'ConvtblInd', YesNoIndicator, False)

	@property
	def CpnRg(self):
		return self._CpnRg

	@CpnRg.setter
	def CpnRg(self, value):
		self._CpnRg = value if value is not None else base_types.UninitialisedField(self, 'CpnRg', AmountOrPercentageRange1, False)

	@CpnRg.deleter
	def CpnRg(self):
		del self._CpnRg
		self._CpnRg = base_types.UninitialisedField(self, 'CpnRg', AmountOrPercentageRange1, False)

	@property
	def CstmDt(self):
		return self._CstmDt

	@CstmDt.setter
	def CstmDt(self, value):
		self._CstmDt = value if value is not None else base_types.UninitialisedField(self, 'CstmDt', DateTimePeriod2, False)

	@CstmDt.deleter
	def CstmDt(self):
		del self._CstmDt
		self._CstmDt = base_types.UninitialisedField(self, 'CstmDt', DateTimePeriod2, False)

	@property
	def EscrwdInd(self):
		return self._EscrwdInd

	@EscrwdInd.setter
	def EscrwdInd(self, value):
		self._EscrwdInd = value if value is not None else base_types.UninitialisedField(self, 'EscrwdInd', YesNoIndicator, False)

	@EscrwdInd.deleter
	def EscrwdInd(self):
		del self._EscrwdInd
		self._EscrwdInd = base_types.UninitialisedField(self, 'EscrwdInd', YesNoIndicator, False)

	@property
	def Geogcs(self):
		return self._Geogcs

	@Geogcs.setter
	def Geogcs(self, value):
		self._Geogcs = value if value is not None else base_types.UninitialisedField(self, 'Geogcs', Max35Text, False)

	@Geogcs.deleter
	def Geogcs(self):
		del self._Geogcs
		self._Geogcs = base_types.UninitialisedField(self, 'Geogcs', Max35Text, False)

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if value is not None else base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@property
	def InsrdInd(self):
		return self._InsrdInd

	@InsrdInd.setter
	def InsrdInd(self, value):
		self._InsrdInd = value if value is not None else base_types.UninitialisedField(self, 'InsrdInd', YesNoIndicator, False)

	@InsrdInd.deleter
	def InsrdInd(self):
		del self._InsrdInd
		self._InsrdInd = base_types.UninitialisedField(self, 'InsrdInd', YesNoIndicator, False)

	@property
	def IsseDt(self):
		return self._IsseDt

	@IsseDt.setter
	def IsseDt(self, value):
		self._IsseDt = value if value is not None else base_types.UninitialisedField(self, 'IsseDt', ISOYearMonth, False)

	@IsseDt.deleter
	def IsseDt(self):
		del self._IsseDt
		self._IsseDt = base_types.UninitialisedField(self, 'IsseDt', ISOYearMonth, False)

	@property
	def IsseSz(self):
		return self._IsseSz

	@IsseSz.setter
	def IsseSz(self, value):
		self._IsseSz = value if value is not None else base_types.UninitialisedField(self, 'IsseSz', Number, False)

	@IsseSz.deleter
	def IsseSz(self):
		del self._IsseSz
		self._IsseSz = base_types.UninitialisedField(self, 'IsseSz', Number, False)

	@property
	def IssrId(self):
		return self._IssrId

	@IssrId.setter
	def IssrId(self, value):
		self._IssrId = value if value is not None else base_types.UninitialisedField(self, 'IssrId', BICNonFIDec2014Identifier, False)

	@IssrId.deleter
	def IssrId(self):
		del self._IssrId
		self._IssrId = base_types.UninitialisedField(self, 'IssrId', BICNonFIDec2014Identifier, False)

	@property
	def LookBck(self):
		return self._LookBck

	@LookBck.setter
	def LookBck(self, value):
		self._LookBck = value if value is not None else base_types.UninitialisedField(self, 'LookBck', Number, False)

	@LookBck.deleter
	def LookBck(self):
		del self._LookBck
		self._LookBck = base_types.UninitialisedField(self, 'LookBck', Number, False)

	@property
	def MaxSbstitn(self):
		return self._MaxSbstitn

	@MaxSbstitn.setter
	def MaxSbstitn(self, value):
		self._MaxSbstitn = value if value is not None else base_types.UninitialisedField(self, 'MaxSbstitn', Number, False)

	@MaxSbstitn.deleter
	def MaxSbstitn(self):
		del self._MaxSbstitn
		self._MaxSbstitn = base_types.UninitialisedField(self, 'MaxSbstitn', Number, False)

	@property
	def MinDnmtn(self):
		return self._MinDnmtn

	@MinDnmtn.setter
	def MinDnmtn(self, value):
		self._MinDnmtn = value if value is not None else base_types.UninitialisedField(self, 'MinDnmtn', FinancialInstrumentQuantity1Choice, False)

	@MinDnmtn.deleter
	def MinDnmtn(self):
		del self._MinDnmtn
		self._MinDnmtn = base_types.UninitialisedField(self, 'MinDnmtn', FinancialInstrumentQuantity1Choice, False)

	@property
	def MinIncrmt(self):
		return self._MinIncrmt

	@MinIncrmt.setter
	def MinIncrmt(self, value):
		self._MinIncrmt = value if value is not None else base_types.UninitialisedField(self, 'MinIncrmt', FinancialInstrumentQuantity1Choice, False)

	@MinIncrmt.deleter
	def MinIncrmt(self):
		del self._MinIncrmt
		self._MinIncrmt = base_types.UninitialisedField(self, 'MinIncrmt', FinancialInstrumentQuantity1Choice, False)

	@property
	def MinQty(self):
		return self._MinQty

	@MinQty.setter
	def MinQty(self, value):
		self._MinQty = value if value is not None else base_types.UninitialisedField(self, 'MinQty', FinancialInstrumentQuantity1Choice, False)

	@MinQty.deleter
	def MinQty(self):
		del self._MinQty
		self._MinQty = base_types.UninitialisedField(self, 'MinQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def MtrtyDt(self):
		return self._MtrtyDt

	@MtrtyDt.setter
	def MtrtyDt(self, value):
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISOYearMonth, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISOYearMonth, False)

	@property
	def OverAlltmtAmt(self):
		return self._OverAlltmtAmt

	@OverAlltmtAmt.setter
	def OverAlltmtAmt(self, value):
		self._OverAlltmtAmt = value if value is not None else base_types.UninitialisedField(self, 'OverAlltmtAmt', ActiveCurrencyAndAmount, False)

	@OverAlltmtAmt.deleter
	def OverAlltmtAmt(self):
		del self._OverAlltmtAmt
		self._OverAlltmtAmt = base_types.UninitialisedField(self, 'OverAlltmtAmt', ActiveCurrencyAndAmount, False)

	@property
	def OverAlltmtRate(self):
		return self._OverAlltmtRate

	@OverAlltmtRate.setter
	def OverAlltmtRate(self, value):
		self._OverAlltmtRate = value if value is not None else base_types.UninitialisedField(self, 'OverAlltmtRate', PercentageRate, False)

	@OverAlltmtRate.deleter
	def OverAlltmtRate(self):
		del self._OverAlltmtRate
		self._OverAlltmtRate = base_types.UninitialisedField(self, 'OverAlltmtRate', PercentageRate, False)

	@property
	def Pdctn(self):
		return self._Pdctn

	@Pdctn.setter
	def Pdctn(self, value):
		self._Pdctn = value if value is not None else base_types.UninitialisedField(self, 'Pdctn', Max35Text, False)

	@Pdctn.deleter
	def Pdctn(self):
		del self._Pdctn
		self._Pdctn = base_types.UninitialisedField(self, 'Pdctn', Max35Text, False)

	@property
	def PerptlInd(self):
		return self._PerptlInd

	@PerptlInd.setter
	def PerptlInd(self, value):
		self._PerptlInd = value if value is not None else base_types.UninitialisedField(self, 'PerptlInd', YesNoIndicator, False)

	@PerptlInd.deleter
	def PerptlInd(self):
		del self._PerptlInd
		self._PerptlInd = base_types.UninitialisedField(self, 'PerptlInd', YesNoIndicator, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', Frequency1Code, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', Frequency1Code, False)

	@property
	def PreFnddInd(self):
		return self._PreFnddInd

	@PreFnddInd.setter
	def PreFnddInd(self, value):
		self._PreFnddInd = value if value is not None else base_types.UninitialisedField(self, 'PreFnddInd', YesNoIndicator, False)

	@PreFnddInd.deleter
	def PreFnddInd(self):
		del self._PreFnddInd
		self._PreFnddInd = base_types.UninitialisedField(self, 'PreFnddInd', YesNoIndicator, False)

	@property
	def PricFrqcy(self):
		return self._PricFrqcy

	@PricFrqcy.setter
	def PricFrqcy(self, value):
		self._PricFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PricFrqcy', Frequency1Code, False)

	@PricFrqcy.deleter
	def PricFrqcy(self):
		del self._PricFrqcy
		self._PricFrqcy = base_types.UninitialisedField(self, 'PricFrqcy', Frequency1Code, False)

	@property
	def PricRg(self):
		return self._PricRg

	@PricRg.setter
	def PricRg(self, value):
		self._PricRg = value if value is not None else base_types.UninitialisedField(self, 'PricRg', AmountOrPercentageRange1, False)

	@PricRg.deleter
	def PricRg(self):
		del self._PricRg
		self._PricRg = base_types.UninitialisedField(self, 'PricRg', AmountOrPercentageRange1, False)

	@property
	def PricSrc(self):
		return self._PricSrc

	@PricSrc.setter
	def PricSrc(self, value):
		self._PricSrc = value if value is not None else base_types.UninitialisedField(self, 'PricSrc', Max35Text, False)

	@PricSrc.deleter
	def PricSrc(self):
		del self._PricSrc
		self._PricSrc = base_types.UninitialisedField(self, 'PricSrc', Max35Text, False)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Max256Text, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Max256Text, False)

	@property
	def PutblInd(self):
		return self._PutblInd

	@PutblInd.setter
	def PutblInd(self, value):
		self._PutblInd = value if value is not None else base_types.UninitialisedField(self, 'PutblInd', YesNoIndicator, False)

	@PutblInd.deleter
	def PutblInd(self):
		del self._PutblInd
		self._PutblInd = base_types.UninitialisedField(self, 'PutblInd', YesNoIndicator, False)

	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if value is not None else base_types.UninitialisedField(self, 'Ratg', Rating1, False)

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = base_types.UninitialisedField(self, 'Ratg', Rating1, False)

	@property
	def RstrctdInd(self):
		return self._RstrctdInd

	@RstrctdInd.setter
	def RstrctdInd(self, value):
		self._RstrctdInd = value if value is not None else base_types.UninitialisedField(self, 'RstrctdInd', YesNoIndicator, False)

	@RstrctdInd.deleter
	def RstrctdInd(self):
		del self._RstrctdInd
		self._RstrctdInd = base_types.UninitialisedField(self, 'RstrctdInd', YesNoIndicator, False)

	@property
	def SbstitnFrqcy(self):
		return self._SbstitnFrqcy

	@SbstitnFrqcy.setter
	def SbstitnFrqcy(self, value):
		self._SbstitnFrqcy = value if value is not None else base_types.UninitialisedField(self, 'SbstitnFrqcy', Frequency1Code, False)

	@SbstitnFrqcy.deleter
	def SbstitnFrqcy(self):
		del self._SbstitnFrqcy
		self._SbstitnFrqcy = base_types.UninitialisedField(self, 'SbstitnFrqcy', Frequency1Code, False)

	@property
	def SbstitnLft(self):
		return self._SbstitnLft

	@SbstitnLft.setter
	def SbstitnLft(self, value):
		self._SbstitnLft = value if value is not None else base_types.UninitialisedField(self, 'SbstitnLft', Number, False)

	@SbstitnLft.deleter
	def SbstitnLft(self):
		del self._SbstitnLft
		self._SbstitnLft = base_types.UninitialisedField(self, 'SbstitnLft', Number, False)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', Max35Text, False)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', Max35Text, False)

	@property
	def TxConds(self):
		return self._TxConds

	@TxConds.setter
	def TxConds(self, value):
		self._TxConds = value if value is not None else base_types.UninitialisedField(self, 'TxConds', TradeTransactionCondition2Code, False)

	@TxConds.deleter
	def TxConds(self):
		del self._TxConds
		self._TxConds = base_types.UninitialisedField(self, 'TxConds', TradeTransactionCondition2Code, False)

	@property
	def WhlPoolInd(self):
		return self._WhlPoolInd

	@WhlPoolInd.setter
	def WhlPoolInd(self, value):
		self._WhlPoolInd = value if value is not None else base_types.UninitialisedField(self, 'WhlPoolInd', YesNoIndicator, False)

	@WhlPoolInd.deleter
	def WhlPoolInd(self):
		del self._WhlPoolInd
		self._WhlPoolInd = base_types.UninitialisedField(self, 'WhlPoolInd', YesNoIndicator, False)

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if value is not None else base_types.UninitialisedField(self, 'XprtnDt', ISODateTime, False)

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = base_types.UninitialisedField(self, 'XprtnDt', ISODateTime, False)

	@property
	def YldRg(self):
		return self._YldRg

	@YldRg.setter
	def YldRg(self, value):
		self._YldRg = value if value is not None else base_types.UninitialisedField(self, 'YldRg', AmountOrPercentageRange1, False)

	@YldRg.deleter
	def YldRg(self):
		del self._YldRg
		self._YldRg = base_types.UninitialisedField(self, 'YldRg', AmountOrPercentageRange1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrntvMinTaxInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtsblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutoRinvstmt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvtblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmDt', type=DateTimePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EscrwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Geogcs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IsseSz', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrId', type=BICNonFIDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LookBck', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSbstitn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinDnmtn', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinIncrmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISOYearMonth, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PerptlInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreFnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ratg', type=Rating1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnFrqcy', type=Frequency1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnLft', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxConds', type=TradeTransactionCondition2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlPoolInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
	))