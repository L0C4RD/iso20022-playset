from . import base_types
from .FundOrderType4Choice import FundOrderType4Choice
from .DeliveryReceiptType2Code import DeliveryReceiptType2Code
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .Equalisation1 import Equalisation1
from .IncomePreference1Code import IncomePreference1Code
from .PaymentTransaction72 import PaymentTransaction72
from .InvestmentFundsOrderBreakdown2 import InvestmentFundsOrderBreakdown2
from .DecimalNumber import DecimalNumber
from .YesNoIndicator import YesNoIndicator
from .PercentageRate import PercentageRate
from .InvestmentAccount58 import InvestmentAccount58
from .FundSettlementParameters11 import FundSettlementParameters11
from .ISODate import ISODate
from .TotalFeesAndTaxes40 import TotalFeesAndTaxes40
from .CustomerConductClassification1Choice import CustomerConductClassification1Choice
from .Max35Text import Max35Text
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .LateReport1Code import LateReport1Code
from .UnitPrice22 import UnitPrice22
from .FinancialAdvice1Code import FinancialAdvice1Code
from .InformativeTax1 import InformativeTax1
from .DeliveryParameters3 import DeliveryParameters3
from .OrderWaiver1 import OrderWaiver1
from .UKTaxGroupUnit1Code import UKTaxGroupUnit1Code
from .Max350Text import Max350Text
from .SignatureType1Choice import SignatureType1Choice
from .ProfitAndLoss2Choice import ProfitAndLoss2Choice
from .RoundingDirection2Code import RoundingDirection2Code
from .HoldBackInformation2 import HoldBackInformation2
from .TransactionChannelType1Choice import TransactionChannelType1Choice
from .ForeignExchangeTerms33 import ForeignExchangeTerms33
from .NegotiatedTrade1Code import NegotiatedTrade1Code
from .IndividualPerson32 import IndividualPerson32
from .Intermediary39 import Intermediary39
from .BestExecution1Code import BestExecution1Code

class RedemptionExecution16(base_types._BaseFieldType):

	__slots__ = ["_PrtlRedWhldgAmt", "_SgntrTp", "_SttlmAndCtdyDtls", "_DealgPricDtls", "_OrdrTp", "_SttlmMtd", "_NgtdTrad", "_IncmPref", "_Rndg", "_UnitsNb", "_BnfcryDtls", "_CumDvddInd", "_TradDtTm", "_PhysDlvryInd", "_StffClntBrkdwn", "_FXDtls", "_Equlstn", "_TxChanlTp", "_DealRef", "_InvstmtAcctDtls", "_CshSttlmDtls", "_LateRpt", "_CstmrCndctClssfctn", "_BestExctn", "_NonStdSttlmInf", "_Grp1Or2Units", "_IntrmPrftAmt", "_OrdrWvrDtls", "_FinAdvc", "_SttlmAmt", "_GtgOrHldBckDtls", "_InftvTaxDtls", "_PrtlSttlmOfCsh", "_PrtlSttlmOfUnits", "_NetAmt", "_PrtlyExctdInd", "_GrssAmt", "_TxOvrhd", "_CshSttlmDt", "_InftvPricDtls", "_RltdPtyDtls", "_PhysDlvryDtls", "_HldgsRedRate", "_OrdrRef", "_ClntRef"]
	@property
	def PrtlRedWhldgAmt(self):
		return self._PrtlRedWhldgAmt

	@PrtlRedWhldgAmt.setter
	def PrtlRedWhldgAmt(self, value):
		self._PrtlRedWhldgAmt = value if type(value) != base_types.auto else self.make_default("PrtlRedWhldgAmt")

	@PrtlRedWhldgAmt.deleter
	def PrtlRedWhldgAmt(self):
		del self._PrtlRedWhldgAmt
		self._PrtlRedWhldgAmt = None

	@property
	def SgntrTp(self):
		return self._SgntrTp

	@SgntrTp.setter
	def SgntrTp(self, value):
		self._SgntrTp = value if type(value) != base_types.auto else self.make_default("SgntrTp")

	@SgntrTp.deleter
	def SgntrTp(self):
		del self._SgntrTp
		self._SgntrTp = None

	@property
	def SttlmAndCtdyDtls(self):
		return self._SttlmAndCtdyDtls

	@SttlmAndCtdyDtls.setter
	def SttlmAndCtdyDtls(self, value):
		self._SttlmAndCtdyDtls = value if type(value) != base_types.auto else self.make_default("SttlmAndCtdyDtls")

	@SttlmAndCtdyDtls.deleter
	def SttlmAndCtdyDtls(self):
		del self._SttlmAndCtdyDtls
		self._SttlmAndCtdyDtls = None

	@property
	def DealgPricDtls(self):
		return self._DealgPricDtls

	@DealgPricDtls.setter
	def DealgPricDtls(self, value):
		self._DealgPricDtls = value if type(value) != base_types.auto else self.make_default("DealgPricDtls")

	@DealgPricDtls.deleter
	def DealgPricDtls(self):
		del self._DealgPricDtls
		self._DealgPricDtls = None

	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if type(value) != base_types.auto else self.make_default("OrdrTp")

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = None

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if type(value) != base_types.auto else self.make_default("SttlmMtd")

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = None

	@property
	def NgtdTrad(self):
		return self._NgtdTrad

	@NgtdTrad.setter
	def NgtdTrad(self, value):
		self._NgtdTrad = value if type(value) != base_types.auto else self.make_default("NgtdTrad")

	@NgtdTrad.deleter
	def NgtdTrad(self):
		del self._NgtdTrad
		self._NgtdTrad = None

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if type(value) != base_types.auto else self.make_default("IncmPref")

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = None

	@property
	def Rndg(self):
		return self._Rndg

	@Rndg.setter
	def Rndg(self, value):
		self._Rndg = value if type(value) != base_types.auto else self.make_default("Rndg")

	@Rndg.deleter
	def Rndg(self):
		del self._Rndg
		self._Rndg = None

	@property
	def UnitsNb(self):
		return self._UnitsNb

	@UnitsNb.setter
	def UnitsNb(self, value):
		self._UnitsNb = value if type(value) != base_types.auto else self.make_default("UnitsNb")

	@UnitsNb.deleter
	def UnitsNb(self):
		del self._UnitsNb
		self._UnitsNb = None

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if type(value) != base_types.auto else self.make_default("BnfcryDtls")

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = None

	@property
	def CumDvddInd(self):
		return self._CumDvddInd

	@CumDvddInd.setter
	def CumDvddInd(self, value):
		self._CumDvddInd = value if type(value) != base_types.auto else self.make_default("CumDvddInd")

	@CumDvddInd.deleter
	def CumDvddInd(self):
		del self._CumDvddInd
		self._CumDvddInd = None

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if type(value) != base_types.auto else self.make_default("TradDtTm")

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = None

	@property
	def PhysDlvryInd(self):
		return self._PhysDlvryInd

	@PhysDlvryInd.setter
	def PhysDlvryInd(self, value):
		self._PhysDlvryInd = value if type(value) != base_types.auto else self.make_default("PhysDlvryInd")

	@PhysDlvryInd.deleter
	def PhysDlvryInd(self):
		del self._PhysDlvryInd
		self._PhysDlvryInd = None

	@property
	def StffClntBrkdwn(self):
		return self._StffClntBrkdwn

	@StffClntBrkdwn.setter
	def StffClntBrkdwn(self, value):
		self._StffClntBrkdwn = value if type(value) != base_types.auto else self.make_default("StffClntBrkdwn")

	@StffClntBrkdwn.deleter
	def StffClntBrkdwn(self):
		del self._StffClntBrkdwn
		self._StffClntBrkdwn = None

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if type(value) != base_types.auto else self.make_default("FXDtls")

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = None

	@property
	def Equlstn(self):
		return self._Equlstn

	@Equlstn.setter
	def Equlstn(self, value):
		self._Equlstn = value if type(value) != base_types.auto else self.make_default("Equlstn")

	@Equlstn.deleter
	def Equlstn(self):
		del self._Equlstn
		self._Equlstn = None

	@property
	def TxChanlTp(self):
		return self._TxChanlTp

	@TxChanlTp.setter
	def TxChanlTp(self, value):
		self._TxChanlTp = value if type(value) != base_types.auto else self.make_default("TxChanlTp")

	@TxChanlTp.deleter
	def TxChanlTp(self):
		del self._TxChanlTp
		self._TxChanlTp = None

	@property
	def DealRef(self):
		return self._DealRef

	@DealRef.setter
	def DealRef(self, value):
		self._DealRef = value if type(value) != base_types.auto else self.make_default("DealRef")

	@DealRef.deleter
	def DealRef(self):
		del self._DealRef
		self._DealRef = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != base_types.auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def CshSttlmDtls(self):
		return self._CshSttlmDtls

	@CshSttlmDtls.setter
	def CshSttlmDtls(self, value):
		self._CshSttlmDtls = value if type(value) != base_types.auto else self.make_default("CshSttlmDtls")

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = None

	@property
	def LateRpt(self):
		return self._LateRpt

	@LateRpt.setter
	def LateRpt(self, value):
		self._LateRpt = value if type(value) != base_types.auto else self.make_default("LateRpt")

	@LateRpt.deleter
	def LateRpt(self):
		del self._LateRpt
		self._LateRpt = None

	@property
	def CstmrCndctClssfctn(self):
		return self._CstmrCndctClssfctn

	@CstmrCndctClssfctn.setter
	def CstmrCndctClssfctn(self, value):
		self._CstmrCndctClssfctn = value if type(value) != base_types.auto else self.make_default("CstmrCndctClssfctn")

	@CstmrCndctClssfctn.deleter
	def CstmrCndctClssfctn(self):
		del self._CstmrCndctClssfctn
		self._CstmrCndctClssfctn = None

	@property
	def BestExctn(self):
		return self._BestExctn

	@BestExctn.setter
	def BestExctn(self, value):
		self._BestExctn = value if type(value) != base_types.auto else self.make_default("BestExctn")

	@BestExctn.deleter
	def BestExctn(self):
		del self._BestExctn
		self._BestExctn = None

	@property
	def NonStdSttlmInf(self):
		return self._NonStdSttlmInf

	@NonStdSttlmInf.setter
	def NonStdSttlmInf(self, value):
		self._NonStdSttlmInf = value if type(value) != base_types.auto else self.make_default("NonStdSttlmInf")

	@NonStdSttlmInf.deleter
	def NonStdSttlmInf(self):
		del self._NonStdSttlmInf
		self._NonStdSttlmInf = None

	@property
	def Grp1Or2Units(self):
		return self._Grp1Or2Units

	@Grp1Or2Units.setter
	def Grp1Or2Units(self, value):
		self._Grp1Or2Units = value if type(value) != base_types.auto else self.make_default("Grp1Or2Units")

	@Grp1Or2Units.deleter
	def Grp1Or2Units(self):
		del self._Grp1Or2Units
		self._Grp1Or2Units = None

	@property
	def IntrmPrftAmt(self):
		return self._IntrmPrftAmt

	@IntrmPrftAmt.setter
	def IntrmPrftAmt(self, value):
		self._IntrmPrftAmt = value if type(value) != base_types.auto else self.make_default("IntrmPrftAmt")

	@IntrmPrftAmt.deleter
	def IntrmPrftAmt(self):
		del self._IntrmPrftAmt
		self._IntrmPrftAmt = None

	@property
	def OrdrWvrDtls(self):
		return self._OrdrWvrDtls

	@OrdrWvrDtls.setter
	def OrdrWvrDtls(self, value):
		self._OrdrWvrDtls = value if type(value) != base_types.auto else self.make_default("OrdrWvrDtls")

	@OrdrWvrDtls.deleter
	def OrdrWvrDtls(self):
		del self._OrdrWvrDtls
		self._OrdrWvrDtls = None

	@property
	def FinAdvc(self):
		return self._FinAdvc

	@FinAdvc.setter
	def FinAdvc(self, value):
		self._FinAdvc = value if type(value) != base_types.auto else self.make_default("FinAdvc")

	@FinAdvc.deleter
	def FinAdvc(self):
		del self._FinAdvc
		self._FinAdvc = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def GtgOrHldBckDtls(self):
		return self._GtgOrHldBckDtls

	@GtgOrHldBckDtls.setter
	def GtgOrHldBckDtls(self, value):
		self._GtgOrHldBckDtls = value if type(value) != base_types.auto else self.make_default("GtgOrHldBckDtls")

	@GtgOrHldBckDtls.deleter
	def GtgOrHldBckDtls(self):
		del self._GtgOrHldBckDtls
		self._GtgOrHldBckDtls = None

	@property
	def InftvTaxDtls(self):
		return self._InftvTaxDtls

	@InftvTaxDtls.setter
	def InftvTaxDtls(self, value):
		self._InftvTaxDtls = value if type(value) != base_types.auto else self.make_default("InftvTaxDtls")

	@InftvTaxDtls.deleter
	def InftvTaxDtls(self):
		del self._InftvTaxDtls
		self._InftvTaxDtls = None

	@property
	def PrtlSttlmOfCsh(self):
		return self._PrtlSttlmOfCsh

	@PrtlSttlmOfCsh.setter
	def PrtlSttlmOfCsh(self, value):
		self._PrtlSttlmOfCsh = value if type(value) != base_types.auto else self.make_default("PrtlSttlmOfCsh")

	@PrtlSttlmOfCsh.deleter
	def PrtlSttlmOfCsh(self):
		del self._PrtlSttlmOfCsh
		self._PrtlSttlmOfCsh = None

	@property
	def PrtlSttlmOfUnits(self):
		return self._PrtlSttlmOfUnits

	@PrtlSttlmOfUnits.setter
	def PrtlSttlmOfUnits(self, value):
		self._PrtlSttlmOfUnits = value if type(value) != base_types.auto else self.make_default("PrtlSttlmOfUnits")

	@PrtlSttlmOfUnits.deleter
	def PrtlSttlmOfUnits(self):
		del self._PrtlSttlmOfUnits
		self._PrtlSttlmOfUnits = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def PrtlyExctdInd(self):
		return self._PrtlyExctdInd

	@PrtlyExctdInd.setter
	def PrtlyExctdInd(self, value):
		self._PrtlyExctdInd = value if type(value) != base_types.auto else self.make_default("PrtlyExctdInd")

	@PrtlyExctdInd.deleter
	def PrtlyExctdInd(self):
		del self._PrtlyExctdInd
		self._PrtlyExctdInd = None

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
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if type(value) != base_types.auto else self.make_default("TxOvrhd")

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = None

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if type(value) != base_types.auto else self.make_default("CshSttlmDt")

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = None

	@property
	def InftvPricDtls(self):
		return self._InftvPricDtls

	@InftvPricDtls.setter
	def InftvPricDtls(self, value):
		self._InftvPricDtls = value if type(value) != base_types.auto else self.make_default("InftvPricDtls")

	@InftvPricDtls.deleter
	def InftvPricDtls(self):
		del self._InftvPricDtls
		self._InftvPricDtls = None

	@property
	def RltdPtyDtls(self):
		return self._RltdPtyDtls

	@RltdPtyDtls.setter
	def RltdPtyDtls(self, value):
		self._RltdPtyDtls = value if type(value) != base_types.auto else self.make_default("RltdPtyDtls")

	@RltdPtyDtls.deleter
	def RltdPtyDtls(self):
		del self._RltdPtyDtls
		self._RltdPtyDtls = None

	@property
	def PhysDlvryDtls(self):
		return self._PhysDlvryDtls

	@PhysDlvryDtls.setter
	def PhysDlvryDtls(self, value):
		self._PhysDlvryDtls = value if type(value) != base_types.auto else self.make_default("PhysDlvryDtls")

	@PhysDlvryDtls.deleter
	def PhysDlvryDtls(self):
		del self._PhysDlvryDtls
		self._PhysDlvryDtls = None

	@property
	def HldgsRedRate(self):
		return self._HldgsRedRate

	@HldgsRedRate.setter
	def HldgsRedRate(self, value):
		self._HldgsRedRate = value if type(value) != base_types.auto else self.make_default("HldgsRedRate")

	@HldgsRedRate.deleter
	def HldgsRedRate(self):
		del self._HldgsRedRate
		self._HldgsRedRate = None

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if type(value) != base_types.auto else self.make_default("OrdrRef")

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = None

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if type(value) != base_types.auto else self.make_default("ClntRef")

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtlRedWhldgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgPricDtls', type=UnitPrice22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=FundOrderType4Choice, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmMtd', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgtdTrad', type=NegotiatedTrade1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsNb', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=IndividualPerson32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StffClntBrkdwn', type=InvestmentFundsOrderBreakdown2, min=0, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms33, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=PaymentTransaction72, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LateRpt', type=LateReport1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BestExctn', type=BestExecution1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmPrftAmt', type=ProfitAndLoss2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrWvrDtls', type=OrderWaiver1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinAdvc', type=FinancialAdvice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GtgOrHldBckDtls', type=HoldBackInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvTaxDtls', type=InformativeTax1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmOfCsh', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmOfUnits', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlyExctdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=TotalFeesAndTaxes40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvPricDtls', type=UnitPrice22, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdPtyDtls', type=Intermediary39, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='PhysDlvryDtls', type=DeliveryParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsRedRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

