# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import ActiveCurrencyCode
from . import AmountOrPercentageRange1
from . import DateTimePeriod1Choice
from . import DecimalNumber
from . import DistributionPolicy2Choice
from . import FinancialInstrumentQuantity1Choice
from . import Frequency35Choice
from . import GlobalNote2Choice
from . import ISODateTime
from . import InstrumentSubStructureType2Choice
from . import InterestType3Code
from . import Max256Text
from . import Max350Text
from . import Max35Text
from . import Max70Text
from . import Number
from . import PaymentDirectionIndicator
from . import PercentageRate
from . import TradeTransactionCondition7Choice
from . import YesNoIndicator
from . import YieldCalculation6

class Debt5(base_types._BaseFieldType):

	__slots__ = ["_ActlDnmtnAmt", "_AltrntvMinTaxInd", "_AmtsblInd", "_AutoRinvstmt", "_BkQlfdInd", "_CPPrgm", "_CPRegnTp", "_CllblInd", "_CpnRg", "_CptlsdIntrst", "_CstPrePmtPnltyInd", "_CstPrePmtYld", "_CurFctr", "_DtdDt", "_EscrwdInd", "_FaceAmt", "_FrstPmtDt", "_GblTp", "_Geogcs", "_Hrcut", "_InsrdInd", "_InstrmStrTp", "_IntrstAcrlDt", "_IntrstClctnMtd", "_IntrstFxgDt", "_IntrstRate", "_IntrstTp", "_LookBck", "_LotId", "_MaxSbstitn", "_MinIncrmt", "_MinQty", "_MtrtyDt", "_NxtCllblDt", "_NxtCpnDt", "_NxtFctr", "_NxtFctrDt", "_NxtIntrstRate", "_OddCpnInd", "_OverAlltmtAmt", "_OverAlltmtRate", "_Pcs", "_Pdctn", "_PerptlInd", "_PlsMax", "_PlsPerLot", "_PlsPerMln", "_PlsPerTrad", "_PmtCcy", "_PmtDrctnInd", "_PmtFrqcy", "_PotntlEuroSysElgblty", "_PreFnddInd", "_PricFrqcy", "_PricRg", "_PricSrc", "_PrvsFctr", "_Purp", "_PutblDt", "_PutblInd", "_RstrctdInd", "_SbstitnFrqcy", "_SbstitnLft", "_Sctr", "_SubrdntdInd", "_TxConds", "_VarblRateInd", "_WghtdAvrgCpn", "_WghtdAvrgLife", "_WghtdAvrgLn", "_WghtdAvrgMtrty", "_WhlPoolInd", "_XprtnDt", "_XtndblInd", "_XtndblPrd", "_YldClctn", "_YldRg"]
	@property
	def ActlDnmtnAmt(self):
		return self._ActlDnmtnAmt

	@ActlDnmtnAmt.setter
	def ActlDnmtnAmt(self, value):
		self._ActlDnmtnAmt = value if value is not None else base_types.UninitialisedField(self, 'ActlDnmtnAmt', ActiveCurrencyAndAmount, True)

	@ActlDnmtnAmt.deleter
	def ActlDnmtnAmt(self):
		del self._ActlDnmtnAmt
		self._ActlDnmtnAmt = base_types.UninitialisedField(self, 'ActlDnmtnAmt', ActiveCurrencyAndAmount, True)

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
	def BkQlfdInd(self):
		return self._BkQlfdInd

	@BkQlfdInd.setter
	def BkQlfdInd(self, value):
		self._BkQlfdInd = value if value is not None else base_types.UninitialisedField(self, 'BkQlfdInd', YesNoIndicator, False)

	@BkQlfdInd.deleter
	def BkQlfdInd(self):
		del self._BkQlfdInd
		self._BkQlfdInd = base_types.UninitialisedField(self, 'BkQlfdInd', YesNoIndicator, False)

	@property
	def CPPrgm(self):
		return self._CPPrgm

	@CPPrgm.setter
	def CPPrgm(self, value):
		self._CPPrgm = value if value is not None else base_types.UninitialisedField(self, 'CPPrgm', Number, False)

	@CPPrgm.deleter
	def CPPrgm(self):
		del self._CPPrgm
		self._CPPrgm = base_types.UninitialisedField(self, 'CPPrgm', Number, False)

	@property
	def CPRegnTp(self):
		return self._CPRegnTp

	@CPRegnTp.setter
	def CPRegnTp(self, value):
		self._CPRegnTp = value if value is not None else base_types.UninitialisedField(self, 'CPRegnTp', Max350Text, False)

	@CPRegnTp.deleter
	def CPRegnTp(self):
		del self._CPRegnTp
		self._CPRegnTp = base_types.UninitialisedField(self, 'CPRegnTp', Max350Text, False)

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
	def CptlsdIntrst(self):
		return self._CptlsdIntrst

	@CptlsdIntrst.setter
	def CptlsdIntrst(self, value):
		self._CptlsdIntrst = value if value is not None else base_types.UninitialisedField(self, 'CptlsdIntrst', DistributionPolicy2Choice, False)

	@CptlsdIntrst.deleter
	def CptlsdIntrst(self):
		del self._CptlsdIntrst
		self._CptlsdIntrst = base_types.UninitialisedField(self, 'CptlsdIntrst', DistributionPolicy2Choice, False)

	@property
	def CstPrePmtPnltyInd(self):
		return self._CstPrePmtPnltyInd

	@CstPrePmtPnltyInd.setter
	def CstPrePmtPnltyInd(self, value):
		self._CstPrePmtPnltyInd = value if value is not None else base_types.UninitialisedField(self, 'CstPrePmtPnltyInd', YesNoIndicator, False)

	@CstPrePmtPnltyInd.deleter
	def CstPrePmtPnltyInd(self):
		del self._CstPrePmtPnltyInd
		self._CstPrePmtPnltyInd = base_types.UninitialisedField(self, 'CstPrePmtPnltyInd', YesNoIndicator, False)

	@property
	def CstPrePmtYld(self):
		return self._CstPrePmtYld

	@CstPrePmtYld.setter
	def CstPrePmtYld(self, value):
		self._CstPrePmtYld = value if value is not None else base_types.UninitialisedField(self, 'CstPrePmtYld', PercentageRate, False)

	@CstPrePmtYld.deleter
	def CstPrePmtYld(self):
		del self._CstPrePmtYld
		self._CstPrePmtYld = base_types.UninitialisedField(self, 'CstPrePmtYld', PercentageRate, False)

	@property
	def CurFctr(self):
		return self._CurFctr

	@CurFctr.setter
	def CurFctr(self, value):
		self._CurFctr = value if value is not None else base_types.UninitialisedField(self, 'CurFctr', PercentageRate, False)

	@CurFctr.deleter
	def CurFctr(self):
		del self._CurFctr
		self._CurFctr = base_types.UninitialisedField(self, 'CurFctr', PercentageRate, False)

	@property
	def DtdDt(self):
		return self._DtdDt

	@DtdDt.setter
	def DtdDt(self, value):
		self._DtdDt = value if value is not None else base_types.UninitialisedField(self, 'DtdDt', ISODateTime, False)

	@DtdDt.deleter
	def DtdDt(self):
		del self._DtdDt
		self._DtdDt = base_types.UninitialisedField(self, 'DtdDt', ISODateTime, False)

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
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if value is not None else base_types.UninitialisedField(self, 'FaceAmt', ActiveCurrencyAndAmount, False)

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = base_types.UninitialisedField(self, 'FaceAmt', ActiveCurrencyAndAmount, False)

	@property
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if value is not None else base_types.UninitialisedField(self, 'FrstPmtDt', ISODateTime, False)

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = base_types.UninitialisedField(self, 'FrstPmtDt', ISODateTime, False)

	@property
	def GblTp(self):
		return self._GblTp

	@GblTp.setter
	def GblTp(self, value):
		self._GblTp = value if value is not None else base_types.UninitialisedField(self, 'GblTp', GlobalNote2Choice, False)

	@GblTp.deleter
	def GblTp(self):
		del self._GblTp
		self._GblTp = base_types.UninitialisedField(self, 'GblTp', GlobalNote2Choice, False)

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
	def InstrmStrTp(self):
		return self._InstrmStrTp

	@InstrmStrTp.setter
	def InstrmStrTp(self, value):
		self._InstrmStrTp = value if value is not None else base_types.UninitialisedField(self, 'InstrmStrTp', InstrumentSubStructureType2Choice, False)

	@InstrmStrTp.deleter
	def InstrmStrTp(self):
		del self._InstrmStrTp
		self._InstrmStrTp = base_types.UninitialisedField(self, 'InstrmStrTp', InstrumentSubStructureType2Choice, False)

	@property
	def IntrstAcrlDt(self):
		return self._IntrstAcrlDt

	@IntrstAcrlDt.setter
	def IntrstAcrlDt(self, value):
		self._IntrstAcrlDt = value if value is not None else base_types.UninitialisedField(self, 'IntrstAcrlDt', ISODateTime, False)

	@IntrstAcrlDt.deleter
	def IntrstAcrlDt(self):
		del self._IntrstAcrlDt
		self._IntrstAcrlDt = base_types.UninitialisedField(self, 'IntrstAcrlDt', ISODateTime, False)

	@property
	def IntrstClctnMtd(self):
		return self._IntrstClctnMtd

	@IntrstClctnMtd.setter
	def IntrstClctnMtd(self, value):
		self._IntrstClctnMtd = value if value is not None else base_types.UninitialisedField(self, 'IntrstClctnMtd', Max70Text, False)

	@IntrstClctnMtd.deleter
	def IntrstClctnMtd(self):
		del self._IntrstClctnMtd
		self._IntrstClctnMtd = base_types.UninitialisedField(self, 'IntrstClctnMtd', Max70Text, False)

	@property
	def IntrstFxgDt(self):
		return self._IntrstFxgDt

	@IntrstFxgDt.setter
	def IntrstFxgDt(self, value):
		self._IntrstFxgDt = value if value is not None else base_types.UninitialisedField(self, 'IntrstFxgDt', ISODateTime, False)

	@IntrstFxgDt.deleter
	def IntrstFxgDt(self):
		del self._IntrstFxgDt
		self._IntrstFxgDt = base_types.UninitialisedField(self, 'IntrstFxgDt', ISODateTime, False)

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if value is not None else base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = base_types.UninitialisedField(self, 'IntrstRate', PercentageRate, False)

	@property
	def IntrstTp(self):
		return self._IntrstTp

	@IntrstTp.setter
	def IntrstTp(self, value):
		self._IntrstTp = value if value is not None else base_types.UninitialisedField(self, 'IntrstTp', InterestType3Code, False)

	@IntrstTp.deleter
	def IntrstTp(self):
		del self._IntrstTp
		self._IntrstTp = base_types.UninitialisedField(self, 'IntrstTp', InterestType3Code, False)

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
	def LotId(self):
		return self._LotId

	@LotId.setter
	def LotId(self, value):
		self._LotId = value if value is not None else base_types.UninitialisedField(self, 'LotId', Max35Text, False)

	@LotId.deleter
	def LotId(self):
		del self._LotId
		self._LotId = base_types.UninitialisedField(self, 'LotId', Max35Text, False)

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
		self._MtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'MtrtyDt', ISODateTime, False)

	@MtrtyDt.deleter
	def MtrtyDt(self):
		del self._MtrtyDt
		self._MtrtyDt = base_types.UninitialisedField(self, 'MtrtyDt', ISODateTime, False)

	@property
	def NxtCllblDt(self):
		return self._NxtCllblDt

	@NxtCllblDt.setter
	def NxtCllblDt(self, value):
		self._NxtCllblDt = value if value is not None else base_types.UninitialisedField(self, 'NxtCllblDt', ISODateTime, False)

	@NxtCllblDt.deleter
	def NxtCllblDt(self):
		del self._NxtCllblDt
		self._NxtCllblDt = base_types.UninitialisedField(self, 'NxtCllblDt', ISODateTime, False)

	@property
	def NxtCpnDt(self):
		return self._NxtCpnDt

	@NxtCpnDt.setter
	def NxtCpnDt(self, value):
		self._NxtCpnDt = value if value is not None else base_types.UninitialisedField(self, 'NxtCpnDt', ISODateTime, False)

	@NxtCpnDt.deleter
	def NxtCpnDt(self):
		del self._NxtCpnDt
		self._NxtCpnDt = base_types.UninitialisedField(self, 'NxtCpnDt', ISODateTime, False)

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if value is not None else base_types.UninitialisedField(self, 'NxtFctr', PercentageRate, False)

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = base_types.UninitialisedField(self, 'NxtFctr', PercentageRate, False)

	@property
	def NxtFctrDt(self):
		return self._NxtFctrDt

	@NxtFctrDt.setter
	def NxtFctrDt(self, value):
		self._NxtFctrDt = value if value is not None else base_types.UninitialisedField(self, 'NxtFctrDt', ISODateTime, False)

	@NxtFctrDt.deleter
	def NxtFctrDt(self):
		del self._NxtFctrDt
		self._NxtFctrDt = base_types.UninitialisedField(self, 'NxtFctrDt', ISODateTime, False)

	@property
	def NxtIntrstRate(self):
		return self._NxtIntrstRate

	@NxtIntrstRate.setter
	def NxtIntrstRate(self, value):
		self._NxtIntrstRate = value if value is not None else base_types.UninitialisedField(self, 'NxtIntrstRate', PercentageRate, False)

	@NxtIntrstRate.deleter
	def NxtIntrstRate(self):
		del self._NxtIntrstRate
		self._NxtIntrstRate = base_types.UninitialisedField(self, 'NxtIntrstRate', PercentageRate, False)

	@property
	def OddCpnInd(self):
		return self._OddCpnInd

	@OddCpnInd.setter
	def OddCpnInd(self, value):
		self._OddCpnInd = value if value is not None else base_types.UninitialisedField(self, 'OddCpnInd', YesNoIndicator, False)

	@OddCpnInd.deleter
	def OddCpnInd(self):
		del self._OddCpnInd
		self._OddCpnInd = base_types.UninitialisedField(self, 'OddCpnInd', YesNoIndicator, False)

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
	def Pcs(self):
		return self._Pcs

	@Pcs.setter
	def Pcs(self, value):
		self._Pcs = value if value is not None else base_types.UninitialisedField(self, 'Pcs', DecimalNumber, False)

	@Pcs.deleter
	def Pcs(self):
		del self._Pcs
		self._Pcs = base_types.UninitialisedField(self, 'Pcs', DecimalNumber, False)

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
	def PlsMax(self):
		return self._PlsMax

	@PlsMax.setter
	def PlsMax(self, value):
		self._PlsMax = value if value is not None else base_types.UninitialisedField(self, 'PlsMax', DecimalNumber, False)

	@PlsMax.deleter
	def PlsMax(self):
		del self._PlsMax
		self._PlsMax = base_types.UninitialisedField(self, 'PlsMax', DecimalNumber, False)

	@property
	def PlsPerLot(self):
		return self._PlsPerLot

	@PlsPerLot.setter
	def PlsPerLot(self, value):
		self._PlsPerLot = value if value is not None else base_types.UninitialisedField(self, 'PlsPerLot', DecimalNumber, False)

	@PlsPerLot.deleter
	def PlsPerLot(self):
		del self._PlsPerLot
		self._PlsPerLot = base_types.UninitialisedField(self, 'PlsPerLot', DecimalNumber, False)

	@property
	def PlsPerMln(self):
		return self._PlsPerMln

	@PlsPerMln.setter
	def PlsPerMln(self, value):
		self._PlsPerMln = value if value is not None else base_types.UninitialisedField(self, 'PlsPerMln', DecimalNumber, False)

	@PlsPerMln.deleter
	def PlsPerMln(self):
		del self._PlsPerMln
		self._PlsPerMln = base_types.UninitialisedField(self, 'PlsPerMln', DecimalNumber, False)

	@property
	def PlsPerTrad(self):
		return self._PlsPerTrad

	@PlsPerTrad.setter
	def PlsPerTrad(self, value):
		self._PlsPerTrad = value if value is not None else base_types.UninitialisedField(self, 'PlsPerTrad', DecimalNumber, False)

	@PlsPerTrad.deleter
	def PlsPerTrad(self):
		del self._PlsPerTrad
		self._PlsPerTrad = base_types.UninitialisedField(self, 'PlsPerTrad', DecimalNumber, False)

	@property
	def PmtCcy(self):
		return self._PmtCcy

	@PmtCcy.setter
	def PmtCcy(self, value):
		self._PmtCcy = value if value is not None else base_types.UninitialisedField(self, 'PmtCcy', ActiveCurrencyCode, False)

	@PmtCcy.deleter
	def PmtCcy(self):
		del self._PmtCcy
		self._PmtCcy = base_types.UninitialisedField(self, 'PmtCcy', ActiveCurrencyCode, False)

	@property
	def PmtDrctnInd(self):
		return self._PmtDrctnInd

	@PmtDrctnInd.setter
	def PmtDrctnInd(self, value):
		self._PmtDrctnInd = value if value is not None else base_types.UninitialisedField(self, 'PmtDrctnInd', PaymentDirectionIndicator, False)

	@PmtDrctnInd.deleter
	def PmtDrctnInd(self):
		del self._PmtDrctnInd
		self._PmtDrctnInd = base_types.UninitialisedField(self, 'PmtDrctnInd', PaymentDirectionIndicator, False)

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PmtFrqcy', Frequency35Choice, False)

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = base_types.UninitialisedField(self, 'PmtFrqcy', Frequency35Choice, False)

	@property
	def PotntlEuroSysElgblty(self):
		return self._PotntlEuroSysElgblty

	@PotntlEuroSysElgblty.setter
	def PotntlEuroSysElgblty(self, value):
		self._PotntlEuroSysElgblty = value if value is not None else base_types.UninitialisedField(self, 'PotntlEuroSysElgblty', YesNoIndicator, False)

	@PotntlEuroSysElgblty.deleter
	def PotntlEuroSysElgblty(self):
		del self._PotntlEuroSysElgblty
		self._PotntlEuroSysElgblty = base_types.UninitialisedField(self, 'PotntlEuroSysElgblty', YesNoIndicator, False)

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
		self._PricFrqcy = value if value is not None else base_types.UninitialisedField(self, 'PricFrqcy', Frequency35Choice, False)

	@PricFrqcy.deleter
	def PricFrqcy(self):
		del self._PricFrqcy
		self._PricFrqcy = base_types.UninitialisedField(self, 'PricFrqcy', Frequency35Choice, False)

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
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if value is not None else base_types.UninitialisedField(self, 'PrvsFctr', PercentageRate, False)

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = base_types.UninitialisedField(self, 'PrvsFctr', PercentageRate, False)

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
	def PutblDt(self):
		return self._PutblDt

	@PutblDt.setter
	def PutblDt(self, value):
		self._PutblDt = value if value is not None else base_types.UninitialisedField(self, 'PutblDt', ISODateTime, False)

	@PutblDt.deleter
	def PutblDt(self):
		del self._PutblDt
		self._PutblDt = base_types.UninitialisedField(self, 'PutblDt', ISODateTime, False)

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
		self._SbstitnFrqcy = value if value is not None else base_types.UninitialisedField(self, 'SbstitnFrqcy', Frequency35Choice, False)

	@SbstitnFrqcy.deleter
	def SbstitnFrqcy(self):
		del self._SbstitnFrqcy
		self._SbstitnFrqcy = base_types.UninitialisedField(self, 'SbstitnFrqcy', Frequency35Choice, False)

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
	def SubrdntdInd(self):
		return self._SubrdntdInd

	@SubrdntdInd.setter
	def SubrdntdInd(self, value):
		self._SubrdntdInd = value if value is not None else base_types.UninitialisedField(self, 'SubrdntdInd', YesNoIndicator, False)

	@SubrdntdInd.deleter
	def SubrdntdInd(self):
		del self._SubrdntdInd
		self._SubrdntdInd = base_types.UninitialisedField(self, 'SubrdntdInd', YesNoIndicator, False)

	@property
	def TxConds(self):
		return self._TxConds

	@TxConds.setter
	def TxConds(self, value):
		self._TxConds = value if value is not None else base_types.UninitialisedField(self, 'TxConds', TradeTransactionCondition7Choice, False)

	@TxConds.deleter
	def TxConds(self):
		del self._TxConds
		self._TxConds = base_types.UninitialisedField(self, 'TxConds', TradeTransactionCondition7Choice, False)

	@property
	def VarblRateInd(self):
		return self._VarblRateInd

	@VarblRateInd.setter
	def VarblRateInd(self, value):
		self._VarblRateInd = value if value is not None else base_types.UninitialisedField(self, 'VarblRateInd', YesNoIndicator, False)

	@VarblRateInd.deleter
	def VarblRateInd(self):
		del self._VarblRateInd
		self._VarblRateInd = base_types.UninitialisedField(self, 'VarblRateInd', YesNoIndicator, False)

	@property
	def WghtdAvrgCpn(self):
		return self._WghtdAvrgCpn

	@WghtdAvrgCpn.setter
	def WghtdAvrgCpn(self, value):
		self._WghtdAvrgCpn = value if value is not None else base_types.UninitialisedField(self, 'WghtdAvrgCpn', PercentageRate, False)

	@WghtdAvrgCpn.deleter
	def WghtdAvrgCpn(self):
		del self._WghtdAvrgCpn
		self._WghtdAvrgCpn = base_types.UninitialisedField(self, 'WghtdAvrgCpn', PercentageRate, False)

	@property
	def WghtdAvrgLife(self):
		return self._WghtdAvrgLife

	@WghtdAvrgLife.setter
	def WghtdAvrgLife(self, value):
		self._WghtdAvrgLife = value if value is not None else base_types.UninitialisedField(self, 'WghtdAvrgLife', DecimalNumber, False)

	@WghtdAvrgLife.deleter
	def WghtdAvrgLife(self):
		del self._WghtdAvrgLife
		self._WghtdAvrgLife = base_types.UninitialisedField(self, 'WghtdAvrgLife', DecimalNumber, False)

	@property
	def WghtdAvrgLn(self):
		return self._WghtdAvrgLn

	@WghtdAvrgLn.setter
	def WghtdAvrgLn(self, value):
		self._WghtdAvrgLn = value if value is not None else base_types.UninitialisedField(self, 'WghtdAvrgLn', DecimalNumber, False)

	@WghtdAvrgLn.deleter
	def WghtdAvrgLn(self):
		del self._WghtdAvrgLn
		self._WghtdAvrgLn = base_types.UninitialisedField(self, 'WghtdAvrgLn', DecimalNumber, False)

	@property
	def WghtdAvrgMtrty(self):
		return self._WghtdAvrgMtrty

	@WghtdAvrgMtrty.setter
	def WghtdAvrgMtrty(self, value):
		self._WghtdAvrgMtrty = value if value is not None else base_types.UninitialisedField(self, 'WghtdAvrgMtrty', DecimalNumber, False)

	@WghtdAvrgMtrty.deleter
	def WghtdAvrgMtrty(self):
		del self._WghtdAvrgMtrty
		self._WghtdAvrgMtrty = base_types.UninitialisedField(self, 'WghtdAvrgMtrty', DecimalNumber, False)

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
	def XtndblInd(self):
		return self._XtndblInd

	@XtndblInd.setter
	def XtndblInd(self, value):
		self._XtndblInd = value if value is not None else base_types.UninitialisedField(self, 'XtndblInd', YesNoIndicator, False)

	@XtndblInd.deleter
	def XtndblInd(self):
		del self._XtndblInd
		self._XtndblInd = base_types.UninitialisedField(self, 'XtndblInd', YesNoIndicator, False)

	@property
	def XtndblPrd(self):
		return self._XtndblPrd

	@XtndblPrd.setter
	def XtndblPrd(self, value):
		self._XtndblPrd = value if value is not None else base_types.UninitialisedField(self, 'XtndblPrd', DateTimePeriod1Choice, False)

	@XtndblPrd.deleter
	def XtndblPrd(self):
		del self._XtndblPrd
		self._XtndblPrd = base_types.UninitialisedField(self, 'XtndblPrd', DateTimePeriod1Choice, False)

	@property
	def YldClctn(self):
		return self._YldClctn

	@YldClctn.setter
	def YldClctn(self, value):
		self._YldClctn = value if value is not None else base_types.UninitialisedField(self, 'YldClctn', YieldCalculation6, True)

	@YldClctn.deleter
	def YldClctn(self):
		del self._YldClctn
		self._YldClctn = base_types.UninitialisedField(self, 'YldClctn', YieldCalculation6, True)

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
		base_types.FieldEntry(name='ActlDnmtnAmt', type=ActiveCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AltrntvMinTaxInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtsblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutoRinvstmt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkQlfdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CPPrgm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CPRegnTp', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlsdIntrst', type=DistributionPolicy2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstPrePmtPnltyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstPrePmtYld', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtdDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EscrwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblTp', type=GlobalNote2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Geogcs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmStrTp', type=InstrumentSubStructureType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrlDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstClctnMtd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxgDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstTp', type=InterestType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LookBck', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSbstitn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinIncrmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCllblDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCpnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctrDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtIntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OddCpnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pcs', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PerptlInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsMax', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsPerLot', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsPerMln', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsPerTrad', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDrctnInd', type=PaymentDirectionIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PotntlEuroSysElgblty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreFnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricFrqcy', type=Frequency35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnFrqcy', type=Frequency35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnLft', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubrdntdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxConds', type=TradeTransactionCondition7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgCpn', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgLife', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgLn', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgMtrty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlPoolInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndblPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldClctn', type=YieldCalculation6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='YldRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
	))