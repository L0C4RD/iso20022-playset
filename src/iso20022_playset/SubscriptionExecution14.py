from . import base_types
import DateAndDateTime2Choice
import SignatureType1Choice
import ActiveCurrencyAndAmount
import TotalFeesAndTaxes42
import TransactionChannelType1Choice
import FundOrderType4Choice
import PercentageRate
import LateReport1Code
import FinancialInstrument57
import RoundingDirection2Code
import SubAccount6
import OrderWaiver1
import ActiveOrHistoricCurrencyCode
import DecimalNumber
import FinancialAdvice1Code
import ISODate
import NegotiatedTrade1Code
import YesNoIndicator
import UnitPrice22
import InvestmentFundsOrderBreakdown2
import Equalisation4
import CustomerConductClassification1Choice
import Intermediary49
import Max35Text
import IncomePreference1Code
import ActiveCurrencyCode
import DeliveryReceiptType2Code
import FundSettlementParameters20
import InformativeTax2
import ForeignExchangeTerms37
import ProfitAndLoss2Choice
import Max350Text
import DeliveryParameters3
import SourceOfCash1Choice
import BestExecution1Code
import PaymentTransaction162

class SubscriptionExecution14(base_types._BaseFieldType):

	__slots__ = ["_PrtlyExctdInd", "_CumDvddInd", "_InftvTaxDtls", "_SttlmAmt", "_IntrmPrftAmt", "_ReqdNAVCcy", "_DealgPricDtls", "_InftvPricDtls", "_CshSttlmDt", "_PrtlSttlmOfCsh", "_StffClntBrkdwn", "_OrdrRef", "_SbcptIntrst", "_AcmltnRghtRef", "_NetAmt", "_LttrInttRef", "_Rndg", "_LateRpt", "_Rfnd", "_ClntRef", "_SttlmAndCtdyDtls", "_PhysDlvryDtls", "_TxChanlTp", "_OrdrTp", "_ReqdSttlmCcy", "_UnitsNb", "_NonStdSttlmInf", "_CshSttlmDtls", "_FXDtls", "_PrtlSttlmOfUnits", "_OrdrWvrDtls", "_IncmPref", "_FinAdvc", "_Equlstn", "_PhysDlvryInd", "_SubAcctForHldg", "_SrcOfCsh", "_NgtdTrad", "_CstmrCndctClssfctn", "_SttlmMtd", "_TradDtTm", "_FinInstrmDtls", "_SgntrTp", "_GrssAmt", "_TxOvrhd", "_BestExctn", "_RltdPtyDtls", "_DealRef"]
	@property
	def PrtlyExctdInd(self):
		return self._PrtlyExctdInd

	@PrtlyExctdInd.setter
	def PrtlyExctdInd(self, value):
		self._PrtlyExctdInd = value if type(value) != auto else self.make_default("PrtlyExctdInd")

	@PrtlyExctdInd.deleter
	def PrtlyExctdInd(self):
		del self._PrtlyExctdInd
		self._PrtlyExctdInd = None

	@property
	def CumDvddInd(self):
		return self._CumDvddInd

	@CumDvddInd.setter
	def CumDvddInd(self, value):
		self._CumDvddInd = value if type(value) != auto else self.make_default("CumDvddInd")

	@CumDvddInd.deleter
	def CumDvddInd(self):
		del self._CumDvddInd
		self._CumDvddInd = None

	@property
	def InftvTaxDtls(self):
		return self._InftvTaxDtls

	@InftvTaxDtls.setter
	def InftvTaxDtls(self, value):
		self._InftvTaxDtls = value if type(value) != auto else self.make_default("InftvTaxDtls")

	@InftvTaxDtls.deleter
	def InftvTaxDtls(self):
		del self._InftvTaxDtls
		self._InftvTaxDtls = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def IntrmPrftAmt(self):
		return self._IntrmPrftAmt

	@IntrmPrftAmt.setter
	def IntrmPrftAmt(self, value):
		self._IntrmPrftAmt = value if type(value) != auto else self.make_default("IntrmPrftAmt")

	@IntrmPrftAmt.deleter
	def IntrmPrftAmt(self):
		del self._IntrmPrftAmt
		self._IntrmPrftAmt = None

	@property
	def ReqdNAVCcy(self):
		return self._ReqdNAVCcy

	@ReqdNAVCcy.setter
	def ReqdNAVCcy(self, value):
		self._ReqdNAVCcy = value if type(value) != auto else self.make_default("ReqdNAVCcy")

	@ReqdNAVCcy.deleter
	def ReqdNAVCcy(self):
		del self._ReqdNAVCcy
		self._ReqdNAVCcy = None

	@property
	def DealgPricDtls(self):
		return self._DealgPricDtls

	@DealgPricDtls.setter
	def DealgPricDtls(self, value):
		self._DealgPricDtls = value if type(value) != auto else self.make_default("DealgPricDtls")

	@DealgPricDtls.deleter
	def DealgPricDtls(self):
		del self._DealgPricDtls
		self._DealgPricDtls = None

	@property
	def InftvPricDtls(self):
		return self._InftvPricDtls

	@InftvPricDtls.setter
	def InftvPricDtls(self, value):
		self._InftvPricDtls = value if type(value) != auto else self.make_default("InftvPricDtls")

	@InftvPricDtls.deleter
	def InftvPricDtls(self):
		del self._InftvPricDtls
		self._InftvPricDtls = None

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if type(value) != auto else self.make_default("CshSttlmDt")

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = None

	@property
	def PrtlSttlmOfCsh(self):
		return self._PrtlSttlmOfCsh

	@PrtlSttlmOfCsh.setter
	def PrtlSttlmOfCsh(self, value):
		self._PrtlSttlmOfCsh = value if type(value) != auto else self.make_default("PrtlSttlmOfCsh")

	@PrtlSttlmOfCsh.deleter
	def PrtlSttlmOfCsh(self):
		del self._PrtlSttlmOfCsh
		self._PrtlSttlmOfCsh = None

	@property
	def StffClntBrkdwn(self):
		return self._StffClntBrkdwn

	@StffClntBrkdwn.setter
	def StffClntBrkdwn(self, value):
		self._StffClntBrkdwn = value if type(value) != auto else self.make_default("StffClntBrkdwn")

	@StffClntBrkdwn.deleter
	def StffClntBrkdwn(self):
		del self._StffClntBrkdwn
		self._StffClntBrkdwn = None

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def SbcptIntrst(self):
		return self._SbcptIntrst

	@SbcptIntrst.setter
	def SbcptIntrst(self, value):
		self._SbcptIntrst = value if type(value) != auto else self.make_default("SbcptIntrst")

	@SbcptIntrst.deleter
	def SbcptIntrst(self):
		del self._SbcptIntrst
		self._SbcptIntrst = None

	@property
	def AcmltnRghtRef(self):
		return self._AcmltnRghtRef

	@AcmltnRghtRef.setter
	def AcmltnRghtRef(self, value):
		self._AcmltnRghtRef = value if type(value) != auto else self.make_default("AcmltnRghtRef")

	@AcmltnRghtRef.deleter
	def AcmltnRghtRef(self):
		del self._AcmltnRghtRef
		self._AcmltnRghtRef = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def LttrInttRef(self):
		return self._LttrInttRef

	@LttrInttRef.setter
	def LttrInttRef(self, value):
		self._LttrInttRef = value if type(value) != auto else self.make_default("LttrInttRef")

	@LttrInttRef.deleter
	def LttrInttRef(self):
		del self._LttrInttRef
		self._LttrInttRef = None

	@property
	def Rndg(self):
		return self._Rndg

	@Rndg.setter
	def Rndg(self, value):
		self._Rndg = value if type(value) != auto else self.make_default("Rndg")

	@Rndg.deleter
	def Rndg(self):
		del self._Rndg
		self._Rndg = None

	@property
	def LateRpt(self):
		return self._LateRpt

	@LateRpt.setter
	def LateRpt(self, value):
		self._LateRpt = value if type(value) != auto else self.make_default("LateRpt")

	@LateRpt.deleter
	def LateRpt(self):
		del self._LateRpt
		self._LateRpt = None

	@property
	def Rfnd(self):
		return self._Rfnd

	@Rfnd.setter
	def Rfnd(self, value):
		self._Rfnd = value if type(value) != auto else self.make_default("Rfnd")

	@Rfnd.deleter
	def Rfnd(self):
		del self._Rfnd
		self._Rfnd = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	@property
	def SttlmAndCtdyDtls(self):
		return self._SttlmAndCtdyDtls

	@SttlmAndCtdyDtls.setter
	def SttlmAndCtdyDtls(self, value):
		self._SttlmAndCtdyDtls = value if type(value) != auto else self.make_default("SttlmAndCtdyDtls")

	@SttlmAndCtdyDtls.deleter
	def SttlmAndCtdyDtls(self):
		del self._SttlmAndCtdyDtls
		self._SttlmAndCtdyDtls = None

	@property
	def PhysDlvryDtls(self):
		return self._PhysDlvryDtls

	@PhysDlvryDtls.setter
	def PhysDlvryDtls(self, value):
		self._PhysDlvryDtls = value if type(value) != auto else self.make_default("PhysDlvryDtls")

	@PhysDlvryDtls.deleter
	def PhysDlvryDtls(self):
		del self._PhysDlvryDtls
		self._PhysDlvryDtls = None

	@property
	def TxChanlTp(self):
		return self._TxChanlTp

	@TxChanlTp.setter
	def TxChanlTp(self, value):
		self._TxChanlTp = value if type(value) != auto else self.make_default("TxChanlTp")

	@TxChanlTp.deleter
	def TxChanlTp(self):
		del self._TxChanlTp
		self._TxChanlTp = None

	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if type(value) != auto else self.make_default("OrdrTp")

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = None

	@property
	def ReqdSttlmCcy(self):
		return self._ReqdSttlmCcy

	@ReqdSttlmCcy.setter
	def ReqdSttlmCcy(self, value):
		self._ReqdSttlmCcy = value if type(value) != auto else self.make_default("ReqdSttlmCcy")

	@ReqdSttlmCcy.deleter
	def ReqdSttlmCcy(self):
		del self._ReqdSttlmCcy
		self._ReqdSttlmCcy = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	@property
	def NonStdSttlmInf(self):
		return self._NonStdSttlmInf

	@NonStdSttlmInf.setter
	def NonStdSttlmInf(self, value):
		self._NonStdSttlmInf = value if type(value) != auto else self.make_default("NonStdSttlmInf")

	@NonStdSttlmInf.deleter
	def NonStdSttlmInf(self):
		del self._NonStdSttlmInf
		self._NonStdSttlmInf = None

	@property
	def CshSttlmDtls(self):
		return self._CshSttlmDtls

	@CshSttlmDtls.setter
	def CshSttlmDtls(self, value):
		self._CshSttlmDtls = value if type(value) != auto else self.make_default("CshSttlmDtls")

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def PrtlSttlmOfUnits(self):
		return self._PrtlSttlmOfUnits

	@PrtlSttlmOfUnits.setter
	def PrtlSttlmOfUnits(self, value):
		self._PrtlSttlmOfUnits = value if type(value) != auto else self.make_default("PrtlSttlmOfUnits")

	@PrtlSttlmOfUnits.deleter
	def PrtlSttlmOfUnits(self):
		del self._PrtlSttlmOfUnits
		self._PrtlSttlmOfUnits = None

	@property
	def OrdrWvrDtls(self):
		return self._OrdrWvrDtls

	@OrdrWvrDtls.setter
	def OrdrWvrDtls(self, value):
		self._OrdrWvrDtls = value if type(value) != auto else self.make_default("OrdrWvrDtls")

	@OrdrWvrDtls.deleter
	def OrdrWvrDtls(self):
		del self._OrdrWvrDtls
		self._OrdrWvrDtls = None

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if type(value) != auto else self.make_default("IncmPref")

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = None

	@property
	def FinAdvc(self):
		return self._FinAdvc

	@FinAdvc.setter
	def FinAdvc(self, value):
		self._FinAdvc = value if type(value) != auto else self.make_default("FinAdvc")

	@FinAdvc.deleter
	def FinAdvc(self):
		del self._FinAdvc
		self._FinAdvc = None

	@property
	def Equlstn(self):
		return self._Equlstn

	@Equlstn.setter
	def Equlstn(self, value):
		self._Equlstn = value if type(value) != auto else self.make_default("Equlstn")

	@Equlstn.deleter
	def Equlstn(self):
		del self._Equlstn
		self._Equlstn = None

	@property
	def PhysDlvryInd(self):
		return self._PhysDlvryInd

	@PhysDlvryInd.setter
	def PhysDlvryInd(self, value):
		self._PhysDlvryInd = value if type(value) != auto else self.make_default("PhysDlvryInd")

	@PhysDlvryInd.deleter
	def PhysDlvryInd(self):
		del self._PhysDlvryInd
		self._PhysDlvryInd = None

	@property
	def SubAcctForHldg(self):
		return self._SubAcctForHldg

	@SubAcctForHldg.setter
	def SubAcctForHldg(self, value):
		self._SubAcctForHldg = value if type(value) != auto else self.make_default("SubAcctForHldg")

	@SubAcctForHldg.deleter
	def SubAcctForHldg(self):
		del self._SubAcctForHldg
		self._SubAcctForHldg = None

	@property
	def SrcOfCsh(self):
		return self._SrcOfCsh

	@SrcOfCsh.setter
	def SrcOfCsh(self, value):
		self._SrcOfCsh = value if type(value) != auto else self.make_default("SrcOfCsh")

	@SrcOfCsh.deleter
	def SrcOfCsh(self):
		del self._SrcOfCsh
		self._SrcOfCsh = None

	@property
	def NgtdTrad(self):
		return self._NgtdTrad

	@NgtdTrad.setter
	def NgtdTrad(self, value):
		self._NgtdTrad = value if type(value) != auto else self.make_default("NgtdTrad")

	@NgtdTrad.deleter
	def NgtdTrad(self):
		del self._NgtdTrad
		self._NgtdTrad = None

	@property
	def CstmrCndctClssfctn(self):
		return self._CstmrCndctClssfctn

	@CstmrCndctClssfctn.setter
	def CstmrCndctClssfctn(self, value):
		self._CstmrCndctClssfctn = value if type(value) != auto else self.make_default("CstmrCndctClssfctn")

	@CstmrCndctClssfctn.deleter
	def CstmrCndctClssfctn(self):
		del self._CstmrCndctClssfctn
		self._CstmrCndctClssfctn = None

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if type(value) != auto else self.make_default("SttlmMtd")

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = None

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if type(value) != auto else self.make_default("TradDtTm")

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	@property
	def SgntrTp(self):
		return self._SgntrTp

	@SgntrTp.setter
	def SgntrTp(self, value):
		self._SgntrTp = value if type(value) != auto else self.make_default("SgntrTp")

	@SgntrTp.deleter
	def SgntrTp(self):
		del self._SgntrTp
		self._SgntrTp = None

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if type(value) != auto else self.make_default("GrssAmt")

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = None

	@property
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if type(value) != auto else self.make_default("TxOvrhd")

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = None

	@property
	def BestExctn(self):
		return self._BestExctn

	@BestExctn.setter
	def BestExctn(self, value):
		self._BestExctn = value if type(value) != auto else self.make_default("BestExctn")

	@BestExctn.deleter
	def BestExctn(self):
		del self._BestExctn
		self._BestExctn = None

	@property
	def RltdPtyDtls(self):
		return self._RltdPtyDtls

	@RltdPtyDtls.setter
	def RltdPtyDtls(self, value):
		self._RltdPtyDtls = value if type(value) != auto else self.make_default("RltdPtyDtls")

	@RltdPtyDtls.deleter
	def RltdPtyDtls(self):
		del self._RltdPtyDtls
		self._RltdPtyDtls = None

	@property
	def DealRef(self):
		return self._DealRef

	@DealRef.setter
	def DealRef(self, value):
		self._DealRef = value if type(value) != auto else self.make_default("DealRef")

	@DealRef.deleter
	def DealRef(self):
		del self._DealRef
		self._DealRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtlyExctdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvTaxDtls', type=InformativeTax2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmPrftAmt', type=ProfitAndLoss2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdNAVCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgPricDtls', type=UnitPrice22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvPricDtls', type=UnitPrice22, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmOfCsh', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StffClntBrkdwn', type=InvestmentFundsOrderBreakdown2, min=0, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptIntrst', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcmltnRghtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrInttRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LateRpt', type=LateReport1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rfnd', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryDtls', type=DeliveryParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=FundOrderType4Choice, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdSttlmCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=PaymentTransaction162, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtlSttlmOfUnits', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrWvrDtls', type=OrderWaiver1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinAdvc', type=FinancialAdvice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=Equalisation4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctForHldg', type=SubAccount6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfCsh', type=SourceOfCash1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NgtdTrad', type=NegotiatedTrade1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument57, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=TotalFeesAndTaxes42, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BestExctn', type=BestExecution1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPtyDtls', type=Intermediary49, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

