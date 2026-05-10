from . import base_types
from .PaymentDirectionIndicator import PaymentDirectionIndicator
from .Max35Text import Max35Text
from .YesNoIndicator import YesNoIndicator
from .PercentageRate import PercentageRate
from .ActiveCurrencyCode import ActiveCurrencyCode
from .Max350Text import Max350Text
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from .GlobalNote2Choice import GlobalNote2Choice
from .Max70Text import Max70Text
from .Number import Number
from .TradeTransactionCondition7Choice import TradeTransactionCondition7Choice
from .AmountOrPercentageRange1 import AmountOrPercentageRange1
from .DistributionPolicy2Choice import DistributionPolicy2Choice
from .DateTimePeriod1Choice import DateTimePeriod1Choice
from .InstrumentSubStructureType2Choice import InstrumentSubStructureType2Choice
from .InterestType3Code import InterestType3Code
from .Frequency35Choice import Frequency35Choice
from .DecimalNumber import DecimalNumber
from .Max256Text import Max256Text
from .ISODateTime import ISODateTime
from .YieldCalculation6 import YieldCalculation6

class Debt5(base_types._BaseFieldType):

	__slots__ = ["_PreFnddInd", "_OverAlltmtRate", "_VarblRateInd", "_MinQty", "_CllblInd", "_PerptlInd", "_PutblDt", "_InstrmStrTp", "_DtdDt", "_GblTp", "_YldRg", "_InsrdInd", "_IntrstClctnMtd", "_Hrcut", "_CurFctr", "_PricRg", "_Geogcs", "_NxtIntrstRate", "_SubrdntdInd", "_IntrstFxgDt", "_WghtdAvrgCpn", "_OverAlltmtAmt", "_CstPrePmtYld", "_CPRegnTp", "_Purp", "_CstPrePmtPnltyInd", "_SbstitnFrqcy", "_PmtCcy", "_AltrntvMinTaxInd", "_AutoRinvstmt", "_WghtdAvrgMtrty", "_ActlDnmtnAmt", "_AmtsblInd", "_PmtDrctnInd", "_BkQlfdInd", "_FaceAmt", "_PlsPerMln", "_MtrtyDt", "_XprtnDt", "_LookBck", "_MaxSbstitn", "_PmtFrqcy", "_NxtCpnDt", "_PricFrqcy", "_WghtdAvrgLife", "_Pdctn", "_TxConds", "_WhlPoolInd", "_CptlsdIntrst", "_CpnRg", "_LotId", "_PrvsFctr", "_PlsPerLot", "_PlsMax", "_IntrstTp", "_PlsPerTrad", "_WghtdAvrgLn", "_YldClctn", "_FrstPmtDt", "_OddCpnInd", "_XtndblPrd", "_EscrwdInd", "_PricSrc", "_IntrstRate", "_XtndblInd", "_RstrctdInd", "_PotntlEuroSysElgblty", "_NxtCllblDt", "_PutblInd", "_Sctr", "_CPPrgm", "_MinIncrmt", "_NxtFctr", "_SbstitnLft", "_Pcs", "_NxtFctrDt", "_IntrstAcrlDt"]
	@property
	def PreFnddInd(self):
		return self._PreFnddInd

	@PreFnddInd.setter
	def PreFnddInd(self, value):
		self._PreFnddInd = value if type(value) != auto else self.make_default("PreFnddInd")

	@PreFnddInd.deleter
	def PreFnddInd(self):
		del self._PreFnddInd
		self._PreFnddInd = None

	@property
	def OverAlltmtRate(self):
		return self._OverAlltmtRate

	@OverAlltmtRate.setter
	def OverAlltmtRate(self, value):
		self._OverAlltmtRate = value if type(value) != auto else self.make_default("OverAlltmtRate")

	@OverAlltmtRate.deleter
	def OverAlltmtRate(self):
		del self._OverAlltmtRate
		self._OverAlltmtRate = None

	@property
	def VarblRateInd(self):
		return self._VarblRateInd

	@VarblRateInd.setter
	def VarblRateInd(self, value):
		self._VarblRateInd = value if type(value) != auto else self.make_default("VarblRateInd")

	@VarblRateInd.deleter
	def VarblRateInd(self):
		del self._VarblRateInd
		self._VarblRateInd = None

	@property
	def MinQty(self):
		return self._MinQty

	@MinQty.setter
	def MinQty(self, value):
		self._MinQty = value if type(value) != auto else self.make_default("MinQty")

	@MinQty.deleter
	def MinQty(self):
		del self._MinQty
		self._MinQty = None

	@property
	def CllblInd(self):
		return self._CllblInd

	@CllblInd.setter
	def CllblInd(self, value):
		self._CllblInd = value if type(value) != auto else self.make_default("CllblInd")

	@CllblInd.deleter
	def CllblInd(self):
		del self._CllblInd
		self._CllblInd = None

	@property
	def PerptlInd(self):
		return self._PerptlInd

	@PerptlInd.setter
	def PerptlInd(self, value):
		self._PerptlInd = value if type(value) != auto else self.make_default("PerptlInd")

	@PerptlInd.deleter
	def PerptlInd(self):
		del self._PerptlInd
		self._PerptlInd = None

	@property
	def PutblDt(self):
		return self._PutblDt

	@PutblDt.setter
	def PutblDt(self, value):
		self._PutblDt = value if type(value) != auto else self.make_default("PutblDt")

	@PutblDt.deleter
	def PutblDt(self):
		del self._PutblDt
		self._PutblDt = None

	@property
	def InstrmStrTp(self):
		return self._InstrmStrTp

	@InstrmStrTp.setter
	def InstrmStrTp(self, value):
		self._InstrmStrTp = value if type(value) != auto else self.make_default("InstrmStrTp")

	@InstrmStrTp.deleter
	def InstrmStrTp(self):
		del self._InstrmStrTp
		self._InstrmStrTp = None

	@property
	def DtdDt(self):
		return self._DtdDt

	@DtdDt.setter
	def DtdDt(self, value):
		self._DtdDt = value if type(value) != auto else self.make_default("DtdDt")

	@DtdDt.deleter
	def DtdDt(self):
		del self._DtdDt
		self._DtdDt = None

	@property
	def GblTp(self):
		return self._GblTp

	@GblTp.setter
	def GblTp(self, value):
		self._GblTp = value if type(value) != auto else self.make_default("GblTp")

	@GblTp.deleter
	def GblTp(self):
		del self._GblTp
		self._GblTp = None

	@property
	def YldRg(self):
		return self._YldRg

	@YldRg.setter
	def YldRg(self, value):
		self._YldRg = value if type(value) != auto else self.make_default("YldRg")

	@YldRg.deleter
	def YldRg(self):
		del self._YldRg
		self._YldRg = None

	@property
	def InsrdInd(self):
		return self._InsrdInd

	@InsrdInd.setter
	def InsrdInd(self, value):
		self._InsrdInd = value if type(value) != auto else self.make_default("InsrdInd")

	@InsrdInd.deleter
	def InsrdInd(self):
		del self._InsrdInd
		self._InsrdInd = None

	@property
	def IntrstClctnMtd(self):
		return self._IntrstClctnMtd

	@IntrstClctnMtd.setter
	def IntrstClctnMtd(self, value):
		self._IntrstClctnMtd = value if type(value) != auto else self.make_default("IntrstClctnMtd")

	@IntrstClctnMtd.deleter
	def IntrstClctnMtd(self):
		del self._IntrstClctnMtd
		self._IntrstClctnMtd = None

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	@property
	def CurFctr(self):
		return self._CurFctr

	@CurFctr.setter
	def CurFctr(self, value):
		self._CurFctr = value if type(value) != auto else self.make_default("CurFctr")

	@CurFctr.deleter
	def CurFctr(self):
		del self._CurFctr
		self._CurFctr = None

	@property
	def PricRg(self):
		return self._PricRg

	@PricRg.setter
	def PricRg(self, value):
		self._PricRg = value if type(value) != auto else self.make_default("PricRg")

	@PricRg.deleter
	def PricRg(self):
		del self._PricRg
		self._PricRg = None

	@property
	def Geogcs(self):
		return self._Geogcs

	@Geogcs.setter
	def Geogcs(self, value):
		self._Geogcs = value if type(value) != auto else self.make_default("Geogcs")

	@Geogcs.deleter
	def Geogcs(self):
		del self._Geogcs
		self._Geogcs = None

	@property
	def NxtIntrstRate(self):
		return self._NxtIntrstRate

	@NxtIntrstRate.setter
	def NxtIntrstRate(self, value):
		self._NxtIntrstRate = value if type(value) != auto else self.make_default("NxtIntrstRate")

	@NxtIntrstRate.deleter
	def NxtIntrstRate(self):
		del self._NxtIntrstRate
		self._NxtIntrstRate = None

	@property
	def SubrdntdInd(self):
		return self._SubrdntdInd

	@SubrdntdInd.setter
	def SubrdntdInd(self, value):
		self._SubrdntdInd = value if type(value) != auto else self.make_default("SubrdntdInd")

	@SubrdntdInd.deleter
	def SubrdntdInd(self):
		del self._SubrdntdInd
		self._SubrdntdInd = None

	@property
	def IntrstFxgDt(self):
		return self._IntrstFxgDt

	@IntrstFxgDt.setter
	def IntrstFxgDt(self, value):
		self._IntrstFxgDt = value if type(value) != auto else self.make_default("IntrstFxgDt")

	@IntrstFxgDt.deleter
	def IntrstFxgDt(self):
		del self._IntrstFxgDt
		self._IntrstFxgDt = None

	@property
	def WghtdAvrgCpn(self):
		return self._WghtdAvrgCpn

	@WghtdAvrgCpn.setter
	def WghtdAvrgCpn(self, value):
		self._WghtdAvrgCpn = value if type(value) != auto else self.make_default("WghtdAvrgCpn")

	@WghtdAvrgCpn.deleter
	def WghtdAvrgCpn(self):
		del self._WghtdAvrgCpn
		self._WghtdAvrgCpn = None

	@property
	def OverAlltmtAmt(self):
		return self._OverAlltmtAmt

	@OverAlltmtAmt.setter
	def OverAlltmtAmt(self, value):
		self._OverAlltmtAmt = value if type(value) != auto else self.make_default("OverAlltmtAmt")

	@OverAlltmtAmt.deleter
	def OverAlltmtAmt(self):
		del self._OverAlltmtAmt
		self._OverAlltmtAmt = None

	@property
	def CstPrePmtYld(self):
		return self._CstPrePmtYld

	@CstPrePmtYld.setter
	def CstPrePmtYld(self, value):
		self._CstPrePmtYld = value if type(value) != auto else self.make_default("CstPrePmtYld")

	@CstPrePmtYld.deleter
	def CstPrePmtYld(self):
		del self._CstPrePmtYld
		self._CstPrePmtYld = None

	@property
	def CPRegnTp(self):
		return self._CPRegnTp

	@CPRegnTp.setter
	def CPRegnTp(self, value):
		self._CPRegnTp = value if type(value) != auto else self.make_default("CPRegnTp")

	@CPRegnTp.deleter
	def CPRegnTp(self):
		del self._CPRegnTp
		self._CPRegnTp = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def CstPrePmtPnltyInd(self):
		return self._CstPrePmtPnltyInd

	@CstPrePmtPnltyInd.setter
	def CstPrePmtPnltyInd(self, value):
		self._CstPrePmtPnltyInd = value if type(value) != auto else self.make_default("CstPrePmtPnltyInd")

	@CstPrePmtPnltyInd.deleter
	def CstPrePmtPnltyInd(self):
		del self._CstPrePmtPnltyInd
		self._CstPrePmtPnltyInd = None

	@property
	def SbstitnFrqcy(self):
		return self._SbstitnFrqcy

	@SbstitnFrqcy.setter
	def SbstitnFrqcy(self, value):
		self._SbstitnFrqcy = value if type(value) != auto else self.make_default("SbstitnFrqcy")

	@SbstitnFrqcy.deleter
	def SbstitnFrqcy(self):
		del self._SbstitnFrqcy
		self._SbstitnFrqcy = None

	@property
	def PmtCcy(self):
		return self._PmtCcy

	@PmtCcy.setter
	def PmtCcy(self, value):
		self._PmtCcy = value if type(value) != auto else self.make_default("PmtCcy")

	@PmtCcy.deleter
	def PmtCcy(self):
		del self._PmtCcy
		self._PmtCcy = None

	@property
	def AltrntvMinTaxInd(self):
		return self._AltrntvMinTaxInd

	@AltrntvMinTaxInd.setter
	def AltrntvMinTaxInd(self, value):
		self._AltrntvMinTaxInd = value if type(value) != auto else self.make_default("AltrntvMinTaxInd")

	@AltrntvMinTaxInd.deleter
	def AltrntvMinTaxInd(self):
		del self._AltrntvMinTaxInd
		self._AltrntvMinTaxInd = None

	@property
	def AutoRinvstmt(self):
		return self._AutoRinvstmt

	@AutoRinvstmt.setter
	def AutoRinvstmt(self, value):
		self._AutoRinvstmt = value if type(value) != auto else self.make_default("AutoRinvstmt")

	@AutoRinvstmt.deleter
	def AutoRinvstmt(self):
		del self._AutoRinvstmt
		self._AutoRinvstmt = None

	@property
	def WghtdAvrgMtrty(self):
		return self._WghtdAvrgMtrty

	@WghtdAvrgMtrty.setter
	def WghtdAvrgMtrty(self, value):
		self._WghtdAvrgMtrty = value if type(value) != auto else self.make_default("WghtdAvrgMtrty")

	@WghtdAvrgMtrty.deleter
	def WghtdAvrgMtrty(self):
		del self._WghtdAvrgMtrty
		self._WghtdAvrgMtrty = None

	@property
	def ActlDnmtnAmt(self):
		return self._ActlDnmtnAmt

	@ActlDnmtnAmt.setter
	def ActlDnmtnAmt(self, value):
		self._ActlDnmtnAmt = value if type(value) != auto else self.make_default("ActlDnmtnAmt")

	@ActlDnmtnAmt.deleter
	def ActlDnmtnAmt(self):
		del self._ActlDnmtnAmt
		self._ActlDnmtnAmt = None

	@property
	def AmtsblInd(self):
		return self._AmtsblInd

	@AmtsblInd.setter
	def AmtsblInd(self, value):
		self._AmtsblInd = value if type(value) != auto else self.make_default("AmtsblInd")

	@AmtsblInd.deleter
	def AmtsblInd(self):
		del self._AmtsblInd
		self._AmtsblInd = None

	@property
	def PmtDrctnInd(self):
		return self._PmtDrctnInd

	@PmtDrctnInd.setter
	def PmtDrctnInd(self, value):
		self._PmtDrctnInd = value if type(value) != auto else self.make_default("PmtDrctnInd")

	@PmtDrctnInd.deleter
	def PmtDrctnInd(self):
		del self._PmtDrctnInd
		self._PmtDrctnInd = None

	@property
	def BkQlfdInd(self):
		return self._BkQlfdInd

	@BkQlfdInd.setter
	def BkQlfdInd(self, value):
		self._BkQlfdInd = value if type(value) != auto else self.make_default("BkQlfdInd")

	@BkQlfdInd.deleter
	def BkQlfdInd(self):
		del self._BkQlfdInd
		self._BkQlfdInd = None

	@property
	def FaceAmt(self):
		return self._FaceAmt

	@FaceAmt.setter
	def FaceAmt(self, value):
		self._FaceAmt = value if type(value) != auto else self.make_default("FaceAmt")

	@FaceAmt.deleter
	def FaceAmt(self):
		del self._FaceAmt
		self._FaceAmt = None

	@property
	def PlsPerMln(self):
		return self._PlsPerMln

	@PlsPerMln.setter
	def PlsPerMln(self, value):
		self._PlsPerMln = value if type(value) != auto else self.make_default("PlsPerMln")

	@PlsPerMln.deleter
	def PlsPerMln(self):
		del self._PlsPerMln
		self._PlsPerMln = None

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
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if type(value) != auto else self.make_default("XprtnDt")

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = None

	@property
	def LookBck(self):
		return self._LookBck

	@LookBck.setter
	def LookBck(self, value):
		self._LookBck = value if type(value) != auto else self.make_default("LookBck")

	@LookBck.deleter
	def LookBck(self):
		del self._LookBck
		self._LookBck = None

	@property
	def MaxSbstitn(self):
		return self._MaxSbstitn

	@MaxSbstitn.setter
	def MaxSbstitn(self, value):
		self._MaxSbstitn = value if type(value) != auto else self.make_default("MaxSbstitn")

	@MaxSbstitn.deleter
	def MaxSbstitn(self):
		del self._MaxSbstitn
		self._MaxSbstitn = None

	@property
	def PmtFrqcy(self):
		return self._PmtFrqcy

	@PmtFrqcy.setter
	def PmtFrqcy(self, value):
		self._PmtFrqcy = value if type(value) != auto else self.make_default("PmtFrqcy")

	@PmtFrqcy.deleter
	def PmtFrqcy(self):
		del self._PmtFrqcy
		self._PmtFrqcy = None

	@property
	def NxtCpnDt(self):
		return self._NxtCpnDt

	@NxtCpnDt.setter
	def NxtCpnDt(self, value):
		self._NxtCpnDt = value if type(value) != auto else self.make_default("NxtCpnDt")

	@NxtCpnDt.deleter
	def NxtCpnDt(self):
		del self._NxtCpnDt
		self._NxtCpnDt = None

	@property
	def PricFrqcy(self):
		return self._PricFrqcy

	@PricFrqcy.setter
	def PricFrqcy(self, value):
		self._PricFrqcy = value if type(value) != auto else self.make_default("PricFrqcy")

	@PricFrqcy.deleter
	def PricFrqcy(self):
		del self._PricFrqcy
		self._PricFrqcy = None

	@property
	def WghtdAvrgLife(self):
		return self._WghtdAvrgLife

	@WghtdAvrgLife.setter
	def WghtdAvrgLife(self, value):
		self._WghtdAvrgLife = value if type(value) != auto else self.make_default("WghtdAvrgLife")

	@WghtdAvrgLife.deleter
	def WghtdAvrgLife(self):
		del self._WghtdAvrgLife
		self._WghtdAvrgLife = None

	@property
	def Pdctn(self):
		return self._Pdctn

	@Pdctn.setter
	def Pdctn(self, value):
		self._Pdctn = value if type(value) != auto else self.make_default("Pdctn")

	@Pdctn.deleter
	def Pdctn(self):
		del self._Pdctn
		self._Pdctn = None

	@property
	def TxConds(self):
		return self._TxConds

	@TxConds.setter
	def TxConds(self, value):
		self._TxConds = value if type(value) != auto else self.make_default("TxConds")

	@TxConds.deleter
	def TxConds(self):
		del self._TxConds
		self._TxConds = None

	@property
	def WhlPoolInd(self):
		return self._WhlPoolInd

	@WhlPoolInd.setter
	def WhlPoolInd(self, value):
		self._WhlPoolInd = value if type(value) != auto else self.make_default("WhlPoolInd")

	@WhlPoolInd.deleter
	def WhlPoolInd(self):
		del self._WhlPoolInd
		self._WhlPoolInd = None

	@property
	def CptlsdIntrst(self):
		return self._CptlsdIntrst

	@CptlsdIntrst.setter
	def CptlsdIntrst(self, value):
		self._CptlsdIntrst = value if type(value) != auto else self.make_default("CptlsdIntrst")

	@CptlsdIntrst.deleter
	def CptlsdIntrst(self):
		del self._CptlsdIntrst
		self._CptlsdIntrst = None

	@property
	def CpnRg(self):
		return self._CpnRg

	@CpnRg.setter
	def CpnRg(self, value):
		self._CpnRg = value if type(value) != auto else self.make_default("CpnRg")

	@CpnRg.deleter
	def CpnRg(self):
		del self._CpnRg
		self._CpnRg = None

	@property
	def LotId(self):
		return self._LotId

	@LotId.setter
	def LotId(self, value):
		self._LotId = value if type(value) != auto else self.make_default("LotId")

	@LotId.deleter
	def LotId(self):
		del self._LotId
		self._LotId = None

	@property
	def PrvsFctr(self):
		return self._PrvsFctr

	@PrvsFctr.setter
	def PrvsFctr(self, value):
		self._PrvsFctr = value if type(value) != auto else self.make_default("PrvsFctr")

	@PrvsFctr.deleter
	def PrvsFctr(self):
		del self._PrvsFctr
		self._PrvsFctr = None

	@property
	def PlsPerLot(self):
		return self._PlsPerLot

	@PlsPerLot.setter
	def PlsPerLot(self, value):
		self._PlsPerLot = value if type(value) != auto else self.make_default("PlsPerLot")

	@PlsPerLot.deleter
	def PlsPerLot(self):
		del self._PlsPerLot
		self._PlsPerLot = None

	@property
	def PlsMax(self):
		return self._PlsMax

	@PlsMax.setter
	def PlsMax(self, value):
		self._PlsMax = value if type(value) != auto else self.make_default("PlsMax")

	@PlsMax.deleter
	def PlsMax(self):
		del self._PlsMax
		self._PlsMax = None

	@property
	def IntrstTp(self):
		return self._IntrstTp

	@IntrstTp.setter
	def IntrstTp(self, value):
		self._IntrstTp = value if type(value) != auto else self.make_default("IntrstTp")

	@IntrstTp.deleter
	def IntrstTp(self):
		del self._IntrstTp
		self._IntrstTp = None

	@property
	def PlsPerTrad(self):
		return self._PlsPerTrad

	@PlsPerTrad.setter
	def PlsPerTrad(self, value):
		self._PlsPerTrad = value if type(value) != auto else self.make_default("PlsPerTrad")

	@PlsPerTrad.deleter
	def PlsPerTrad(self):
		del self._PlsPerTrad
		self._PlsPerTrad = None

	@property
	def WghtdAvrgLn(self):
		return self._WghtdAvrgLn

	@WghtdAvrgLn.setter
	def WghtdAvrgLn(self, value):
		self._WghtdAvrgLn = value if type(value) != auto else self.make_default("WghtdAvrgLn")

	@WghtdAvrgLn.deleter
	def WghtdAvrgLn(self):
		del self._WghtdAvrgLn
		self._WghtdAvrgLn = None

	@property
	def YldClctn(self):
		return self._YldClctn

	@YldClctn.setter
	def YldClctn(self, value):
		self._YldClctn = value if type(value) != auto else self.make_default("YldClctn")

	@YldClctn.deleter
	def YldClctn(self):
		del self._YldClctn
		self._YldClctn = None

	@property
	def FrstPmtDt(self):
		return self._FrstPmtDt

	@FrstPmtDt.setter
	def FrstPmtDt(self, value):
		self._FrstPmtDt = value if type(value) != auto else self.make_default("FrstPmtDt")

	@FrstPmtDt.deleter
	def FrstPmtDt(self):
		del self._FrstPmtDt
		self._FrstPmtDt = None

	@property
	def OddCpnInd(self):
		return self._OddCpnInd

	@OddCpnInd.setter
	def OddCpnInd(self, value):
		self._OddCpnInd = value if type(value) != auto else self.make_default("OddCpnInd")

	@OddCpnInd.deleter
	def OddCpnInd(self):
		del self._OddCpnInd
		self._OddCpnInd = None

	@property
	def XtndblPrd(self):
		return self._XtndblPrd

	@XtndblPrd.setter
	def XtndblPrd(self, value):
		self._XtndblPrd = value if type(value) != auto else self.make_default("XtndblPrd")

	@XtndblPrd.deleter
	def XtndblPrd(self):
		del self._XtndblPrd
		self._XtndblPrd = None

	@property
	def EscrwdInd(self):
		return self._EscrwdInd

	@EscrwdInd.setter
	def EscrwdInd(self, value):
		self._EscrwdInd = value if type(value) != auto else self.make_default("EscrwdInd")

	@EscrwdInd.deleter
	def EscrwdInd(self):
		del self._EscrwdInd
		self._EscrwdInd = None

	@property
	def PricSrc(self):
		return self._PricSrc

	@PricSrc.setter
	def PricSrc(self, value):
		self._PricSrc = value if type(value) != auto else self.make_default("PricSrc")

	@PricSrc.deleter
	def PricSrc(self):
		del self._PricSrc
		self._PricSrc = None

	@property
	def IntrstRate(self):
		return self._IntrstRate

	@IntrstRate.setter
	def IntrstRate(self, value):
		self._IntrstRate = value if type(value) != auto else self.make_default("IntrstRate")

	@IntrstRate.deleter
	def IntrstRate(self):
		del self._IntrstRate
		self._IntrstRate = None

	@property
	def XtndblInd(self):
		return self._XtndblInd

	@XtndblInd.setter
	def XtndblInd(self, value):
		self._XtndblInd = value if type(value) != auto else self.make_default("XtndblInd")

	@XtndblInd.deleter
	def XtndblInd(self):
		del self._XtndblInd
		self._XtndblInd = None

	@property
	def RstrctdInd(self):
		return self._RstrctdInd

	@RstrctdInd.setter
	def RstrctdInd(self, value):
		self._RstrctdInd = value if type(value) != auto else self.make_default("RstrctdInd")

	@RstrctdInd.deleter
	def RstrctdInd(self):
		del self._RstrctdInd
		self._RstrctdInd = None

	@property
	def PotntlEuroSysElgblty(self):
		return self._PotntlEuroSysElgblty

	@PotntlEuroSysElgblty.setter
	def PotntlEuroSysElgblty(self, value):
		self._PotntlEuroSysElgblty = value if type(value) != auto else self.make_default("PotntlEuroSysElgblty")

	@PotntlEuroSysElgblty.deleter
	def PotntlEuroSysElgblty(self):
		del self._PotntlEuroSysElgblty
		self._PotntlEuroSysElgblty = None

	@property
	def NxtCllblDt(self):
		return self._NxtCllblDt

	@NxtCllblDt.setter
	def NxtCllblDt(self, value):
		self._NxtCllblDt = value if type(value) != auto else self.make_default("NxtCllblDt")

	@NxtCllblDt.deleter
	def NxtCllblDt(self):
		del self._NxtCllblDt
		self._NxtCllblDt = None

	@property
	def PutblInd(self):
		return self._PutblInd

	@PutblInd.setter
	def PutblInd(self, value):
		self._PutblInd = value if type(value) != auto else self.make_default("PutblInd")

	@PutblInd.deleter
	def PutblInd(self):
		del self._PutblInd
		self._PutblInd = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	@property
	def CPPrgm(self):
		return self._CPPrgm

	@CPPrgm.setter
	def CPPrgm(self, value):
		self._CPPrgm = value if type(value) != auto else self.make_default("CPPrgm")

	@CPPrgm.deleter
	def CPPrgm(self):
		del self._CPPrgm
		self._CPPrgm = None

	@property
	def MinIncrmt(self):
		return self._MinIncrmt

	@MinIncrmt.setter
	def MinIncrmt(self, value):
		self._MinIncrmt = value if type(value) != auto else self.make_default("MinIncrmt")

	@MinIncrmt.deleter
	def MinIncrmt(self):
		del self._MinIncrmt
		self._MinIncrmt = None

	@property
	def NxtFctr(self):
		return self._NxtFctr

	@NxtFctr.setter
	def NxtFctr(self, value):
		self._NxtFctr = value if type(value) != auto else self.make_default("NxtFctr")

	@NxtFctr.deleter
	def NxtFctr(self):
		del self._NxtFctr
		self._NxtFctr = None

	@property
	def SbstitnLft(self):
		return self._SbstitnLft

	@SbstitnLft.setter
	def SbstitnLft(self, value):
		self._SbstitnLft = value if type(value) != auto else self.make_default("SbstitnLft")

	@SbstitnLft.deleter
	def SbstitnLft(self):
		del self._SbstitnLft
		self._SbstitnLft = None

	@property
	def Pcs(self):
		return self._Pcs

	@Pcs.setter
	def Pcs(self, value):
		self._Pcs = value if type(value) != auto else self.make_default("Pcs")

	@Pcs.deleter
	def Pcs(self):
		del self._Pcs
		self._Pcs = None

	@property
	def NxtFctrDt(self):
		return self._NxtFctrDt

	@NxtFctrDt.setter
	def NxtFctrDt(self, value):
		self._NxtFctrDt = value if type(value) != auto else self.make_default("NxtFctrDt")

	@NxtFctrDt.deleter
	def NxtFctrDt(self):
		del self._NxtFctrDt
		self._NxtFctrDt = None

	@property
	def IntrstAcrlDt(self):
		return self._IntrstAcrlDt

	@IntrstAcrlDt.setter
	def IntrstAcrlDt(self, value):
		self._IntrstAcrlDt = value if type(value) != auto else self.make_default("IntrstAcrlDt")

	@IntrstAcrlDt.deleter
	def IntrstAcrlDt(self):
		del self._IntrstAcrlDt
		self._IntrstAcrlDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PreFnddInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VarblRateInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinQty', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CllblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PerptlInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrmStrTp', type=InstrumentSubStructureType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtdDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblTp', type=GlobalNote2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InsrdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstClctnMtd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CurFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Geogcs', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtIntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubrdntdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstFxgDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgCpn', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OverAlltmtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstPrePmtYld', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CPRegnTp', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstPrePmtPnltyInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnFrqcy', type=Frequency35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AltrntvMinTaxInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AutoRinvstmt', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgMtrty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ActlDnmtnAmt', type=ActiveCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AmtsblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDrctnInd', type=PaymentDirectionIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BkQlfdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FaceAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsPerMln', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtrtyDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LookBck', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxSbstitn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtFrqcy', type=Frequency35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCpnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricFrqcy', type=Frequency35Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgLife', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxConds', type=TradeTransactionCondition7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WhlPoolInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CptlsdIntrst', type=DistributionPolicy2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpnRg', type=AmountOrPercentageRange1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsPerLot', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsMax', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstTp', type=InterestType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlsPerTrad', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WghtdAvrgLn', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='YldClctn', type=YieldCalculation6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrstPmtDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OddCpnInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndblPrd', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EscrwdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSrc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PotntlEuroSysElgblty', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtCllblDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutblInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CPPrgm', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinIncrmt', type=FinancialInstrumentQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbstitnLft', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pcs', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NxtFctrDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrstAcrlDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

