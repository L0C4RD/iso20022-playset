# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BestExecution1Code
from . import CustomerConductClassification1Choice
from . import DateAndDateTime2Choice
from . import DeliveryParameters3
from . import DeliveryReceiptType2Code
from . import DigitalPaymentSettlement3
from . import Equalisation1
from . import FinancialAdvice1Code
from . import ForeignExchangeTerms37
from . import FundOrderType4Choice
from . import FundSettlementParameters22
from . import HoldBackInformation5
from . import ISODate
from . import IncomePreference1Code
from . import IndividualPerson32
from . import InformativeTax2
from . import Intermediary49
from . import InvestmentAccount81
from . import InvestmentFundsOrderBreakdown2
from . import LateReport1Code
from . import Max350Text
from . import Max35Text
from . import NegotiatedTrade1Code
from . import OrderWaiver1
from . import PaymentTransaction167
from . import PercentageRate
from . import ProfitAndLoss2Choice
from . import RoundingDirection2Code
from . import SignatureType1Choice
from . import TotalFeesAndTaxes45
from . import TransactionChannelType1Choice
from . import UKTaxGroupUnit1Code
from . import Unit1Choice
from . import UnitPrice22
from . import YesNoIndicator

class RedemptionExecution18(base_types._BaseFieldType):

	__slots__ = ["_BestExctn", "_BnfcryDtls", "_ClntRef", "_CshSttlmDt", "_CshSttlmDtls", "_CstmrCndctClssfctn", "_CumDvddInd", "_DealRef", "_DealgPricDtls", "_DgtlAsstSttlm", "_Equlstn", "_FXDtls", "_FinAdvc", "_Grp1Or2Units", "_GrssAmt", "_GtgOrHldBckDtls", "_HldgsRedRate", "_IncmPref", "_InftvPricDtls", "_InftvTaxDtls", "_IntrmPrftAmt", "_InvstmtAcctDtls", "_LateRpt", "_NetAmt", "_NgtdTrad", "_NonStdSttlmInf", "_NonceId", "_OrdrRef", "_OrdrTp", "_OrdrWvrDtls", "_PhysDlvryDtls", "_PhysDlvryInd", "_PrtlRedWhldgAmt", "_PrtlSttlmOfCsh", "_PrtlSttlmOfUnits", "_PrtlyExctdInd", "_RltdPtyDtls", "_Rndg", "_SgntrTp", "_StffClntBrkdwn", "_SttlmAmt", "_SttlmAndCtdyDtls", "_SttlmMtd", "_TradDtTm", "_TxChanlTp", "_TxOvrhd", "_Units"]
	@property
	def BestExctn(self):
		return self._BestExctn

	@BestExctn.setter
	def BestExctn(self, value):
		self._BestExctn = value if value is not None else base_types.UninitialisedField(self, 'BestExctn', BestExecution1Code, False)

	@BestExctn.deleter
	def BestExctn(self):
		del self._BestExctn
		self._BestExctn = base_types.UninitialisedField(self, 'BestExctn', BestExecution1Code, False)

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if value is not None else base_types.UninitialisedField(self, 'BnfcryDtls', IndividualPerson32, True)

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = base_types.UninitialisedField(self, 'BnfcryDtls', IndividualPerson32, True)

	@property
	def ClntRef(self):
		return self._ClntRef

	@ClntRef.setter
	def ClntRef(self, value):
		self._ClntRef = value if value is not None else base_types.UninitialisedField(self, 'ClntRef', Max35Text, False)

	@ClntRef.deleter
	def ClntRef(self):
		del self._ClntRef
		self._ClntRef = base_types.UninitialisedField(self, 'ClntRef', Max35Text, False)

	@property
	def CshSttlmDt(self):
		return self._CshSttlmDt

	@CshSttlmDt.setter
	def CshSttlmDt(self, value):
		self._CshSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDt', ISODate, False)

	@CshSttlmDt.deleter
	def CshSttlmDt(self):
		del self._CshSttlmDt
		self._CshSttlmDt = base_types.UninitialisedField(self, 'CshSttlmDt', ISODate, False)

	@property
	def CshSttlmDtls(self):
		return self._CshSttlmDtls

	@CshSttlmDtls.setter
	def CshSttlmDtls(self, value):
		self._CshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDtls', PaymentTransaction167, False)

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = base_types.UninitialisedField(self, 'CshSttlmDtls', PaymentTransaction167, False)

	@property
	def CstmrCndctClssfctn(self):
		return self._CstmrCndctClssfctn

	@CstmrCndctClssfctn.setter
	def CstmrCndctClssfctn(self, value):
		self._CstmrCndctClssfctn = value if value is not None else base_types.UninitialisedField(self, 'CstmrCndctClssfctn', CustomerConductClassification1Choice, False)

	@CstmrCndctClssfctn.deleter
	def CstmrCndctClssfctn(self):
		del self._CstmrCndctClssfctn
		self._CstmrCndctClssfctn = base_types.UninitialisedField(self, 'CstmrCndctClssfctn', CustomerConductClassification1Choice, False)

	@property
	def CumDvddInd(self):
		return self._CumDvddInd

	@CumDvddInd.setter
	def CumDvddInd(self, value):
		self._CumDvddInd = value if value is not None else base_types.UninitialisedField(self, 'CumDvddInd', YesNoIndicator, False)

	@CumDvddInd.deleter
	def CumDvddInd(self):
		del self._CumDvddInd
		self._CumDvddInd = base_types.UninitialisedField(self, 'CumDvddInd', YesNoIndicator, False)

	@property
	def DealRef(self):
		return self._DealRef

	@DealRef.setter
	def DealRef(self, value):
		self._DealRef = value if value is not None else base_types.UninitialisedField(self, 'DealRef', Max35Text, False)

	@DealRef.deleter
	def DealRef(self):
		del self._DealRef
		self._DealRef = base_types.UninitialisedField(self, 'DealRef', Max35Text, False)

	@property
	def DealgPricDtls(self):
		return self._DealgPricDtls

	@DealgPricDtls.setter
	def DealgPricDtls(self, value):
		self._DealgPricDtls = value if value is not None else base_types.UninitialisedField(self, 'DealgPricDtls', UnitPrice22, False)

	@DealgPricDtls.deleter
	def DealgPricDtls(self):
		del self._DealgPricDtls
		self._DealgPricDtls = base_types.UninitialisedField(self, 'DealgPricDtls', UnitPrice22, False)

	@property
	def DgtlAsstSttlm(self):
		return self._DgtlAsstSttlm

	@DgtlAsstSttlm.setter
	def DgtlAsstSttlm(self, value):
		self._DgtlAsstSttlm = value if value is not None else base_types.UninitialisedField(self, 'DgtlAsstSttlm', DigitalPaymentSettlement3, False)

	@DgtlAsstSttlm.deleter
	def DgtlAsstSttlm(self):
		del self._DgtlAsstSttlm
		self._DgtlAsstSttlm = base_types.UninitialisedField(self, 'DgtlAsstSttlm', DigitalPaymentSettlement3, False)

	@property
	def Equlstn(self):
		return self._Equlstn

	@Equlstn.setter
	def Equlstn(self, value):
		self._Equlstn = value if value is not None else base_types.UninitialisedField(self, 'Equlstn', Equalisation1, False)

	@Equlstn.deleter
	def Equlstn(self):
		del self._Equlstn
		self._Equlstn = base_types.UninitialisedField(self, 'Equlstn', Equalisation1, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms37, True)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms37, True)

	@property
	def FinAdvc(self):
		return self._FinAdvc

	@FinAdvc.setter
	def FinAdvc(self, value):
		self._FinAdvc = value if value is not None else base_types.UninitialisedField(self, 'FinAdvc', FinancialAdvice1Code, False)

	@FinAdvc.deleter
	def FinAdvc(self):
		del self._FinAdvc
		self._FinAdvc = base_types.UninitialisedField(self, 'FinAdvc', FinancialAdvice1Code, False)

	@property
	def Grp1Or2Units(self):
		return self._Grp1Or2Units

	@Grp1Or2Units.setter
	def Grp1Or2Units(self, value):
		self._Grp1Or2Units = value if value is not None else base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@Grp1Or2Units.deleter
	def Grp1Or2Units(self):
		del self._Grp1Or2Units
		self._Grp1Or2Units = base_types.UninitialisedField(self, 'Grp1Or2Units', UKTaxGroupUnit1Code, False)

	@property
	def GrssAmt(self):
		return self._GrssAmt

	@GrssAmt.setter
	def GrssAmt(self, value):
		self._GrssAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssAmt', ActiveCurrencyAndAmount, False)

	@GrssAmt.deleter
	def GrssAmt(self):
		del self._GrssAmt
		self._GrssAmt = base_types.UninitialisedField(self, 'GrssAmt', ActiveCurrencyAndAmount, False)

	@property
	def GtgOrHldBckDtls(self):
		return self._GtgOrHldBckDtls

	@GtgOrHldBckDtls.setter
	def GtgOrHldBckDtls(self, value):
		self._GtgOrHldBckDtls = value if value is not None else base_types.UninitialisedField(self, 'GtgOrHldBckDtls', HoldBackInformation5, False)

	@GtgOrHldBckDtls.deleter
	def GtgOrHldBckDtls(self):
		del self._GtgOrHldBckDtls
		self._GtgOrHldBckDtls = base_types.UninitialisedField(self, 'GtgOrHldBckDtls', HoldBackInformation5, False)

	@property
	def HldgsRedRate(self):
		return self._HldgsRedRate

	@HldgsRedRate.setter
	def HldgsRedRate(self, value):
		self._HldgsRedRate = value if value is not None else base_types.UninitialisedField(self, 'HldgsRedRate', PercentageRate, False)

	@HldgsRedRate.deleter
	def HldgsRedRate(self):
		del self._HldgsRedRate
		self._HldgsRedRate = base_types.UninitialisedField(self, 'HldgsRedRate', PercentageRate, False)

	@property
	def IncmPref(self):
		return self._IncmPref

	@IncmPref.setter
	def IncmPref(self, value):
		self._IncmPref = value if value is not None else base_types.UninitialisedField(self, 'IncmPref', IncomePreference1Code, False)

	@IncmPref.deleter
	def IncmPref(self):
		del self._IncmPref
		self._IncmPref = base_types.UninitialisedField(self, 'IncmPref', IncomePreference1Code, False)

	@property
	def InftvPricDtls(self):
		return self._InftvPricDtls

	@InftvPricDtls.setter
	def InftvPricDtls(self, value):
		self._InftvPricDtls = value if value is not None else base_types.UninitialisedField(self, 'InftvPricDtls', UnitPrice22, True)

	@InftvPricDtls.deleter
	def InftvPricDtls(self):
		del self._InftvPricDtls
		self._InftvPricDtls = base_types.UninitialisedField(self, 'InftvPricDtls', UnitPrice22, True)

	@property
	def InftvTaxDtls(self):
		return self._InftvTaxDtls

	@InftvTaxDtls.setter
	def InftvTaxDtls(self, value):
		self._InftvTaxDtls = value if value is not None else base_types.UninitialisedField(self, 'InftvTaxDtls', InformativeTax2, False)

	@InftvTaxDtls.deleter
	def InftvTaxDtls(self):
		del self._InftvTaxDtls
		self._InftvTaxDtls = base_types.UninitialisedField(self, 'InftvTaxDtls', InformativeTax2, False)

	@property
	def IntrmPrftAmt(self):
		return self._IntrmPrftAmt

	@IntrmPrftAmt.setter
	def IntrmPrftAmt(self, value):
		self._IntrmPrftAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrmPrftAmt', ProfitAndLoss2Choice, False)

	@IntrmPrftAmt.deleter
	def IntrmPrftAmt(self):
		del self._IntrmPrftAmt
		self._IntrmPrftAmt = base_types.UninitialisedField(self, 'IntrmPrftAmt', ProfitAndLoss2Choice, False)

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if value is not None else base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount81, False)

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = base_types.UninitialisedField(self, 'InvstmtAcctDtls', InvestmentAccount81, False)

	@property
	def LateRpt(self):
		return self._LateRpt

	@LateRpt.setter
	def LateRpt(self, value):
		self._LateRpt = value if value is not None else base_types.UninitialisedField(self, 'LateRpt', LateReport1Code, False)

	@LateRpt.deleter
	def LateRpt(self):
		del self._LateRpt
		self._LateRpt = base_types.UninitialisedField(self, 'LateRpt', LateReport1Code, False)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', ActiveCurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', ActiveCurrencyAndAmount, False)

	@property
	def NgtdTrad(self):
		return self._NgtdTrad

	@NgtdTrad.setter
	def NgtdTrad(self, value):
		self._NgtdTrad = value if value is not None else base_types.UninitialisedField(self, 'NgtdTrad', NegotiatedTrade1Code, False)

	@NgtdTrad.deleter
	def NgtdTrad(self):
		del self._NgtdTrad
		self._NgtdTrad = base_types.UninitialisedField(self, 'NgtdTrad', NegotiatedTrade1Code, False)

	@property
	def NonStdSttlmInf(self):
		return self._NonStdSttlmInf

	@NonStdSttlmInf.setter
	def NonStdSttlmInf(self, value):
		self._NonStdSttlmInf = value if value is not None else base_types.UninitialisedField(self, 'NonStdSttlmInf', Max350Text, False)

	@NonStdSttlmInf.deleter
	def NonStdSttlmInf(self):
		del self._NonStdSttlmInf
		self._NonStdSttlmInf = base_types.UninitialisedField(self, 'NonStdSttlmInf', Max350Text, False)

	@property
	def NonceId(self):
		return self._NonceId

	@NonceId.setter
	def NonceId(self, value):
		self._NonceId = value if value is not None else base_types.UninitialisedField(self, 'NonceId', Max35Text, False)

	@NonceId.deleter
	def NonceId(self):
		del self._NonceId
		self._NonceId = base_types.UninitialisedField(self, 'NonceId', Max35Text, False)

	@property
	def OrdrRef(self):
		return self._OrdrRef

	@OrdrRef.setter
	def OrdrRef(self, value):
		self._OrdrRef = value if value is not None else base_types.UninitialisedField(self, 'OrdrRef', Max35Text, False)

	@OrdrRef.deleter
	def OrdrRef(self):
		del self._OrdrRef
		self._OrdrRef = base_types.UninitialisedField(self, 'OrdrRef', Max35Text, False)

	@property
	def OrdrTp(self):
		return self._OrdrTp

	@OrdrTp.setter
	def OrdrTp(self, value):
		self._OrdrTp = value if value is not None else base_types.UninitialisedField(self, 'OrdrTp', FundOrderType4Choice, True)

	@OrdrTp.deleter
	def OrdrTp(self):
		del self._OrdrTp
		self._OrdrTp = base_types.UninitialisedField(self, 'OrdrTp', FundOrderType4Choice, True)

	@property
	def OrdrWvrDtls(self):
		return self._OrdrWvrDtls

	@OrdrWvrDtls.setter
	def OrdrWvrDtls(self, value):
		self._OrdrWvrDtls = value if value is not None else base_types.UninitialisedField(self, 'OrdrWvrDtls', OrderWaiver1, False)

	@OrdrWvrDtls.deleter
	def OrdrWvrDtls(self):
		del self._OrdrWvrDtls
		self._OrdrWvrDtls = base_types.UninitialisedField(self, 'OrdrWvrDtls', OrderWaiver1, False)

	@property
	def PhysDlvryDtls(self):
		return self._PhysDlvryDtls

	@PhysDlvryDtls.setter
	def PhysDlvryDtls(self, value):
		self._PhysDlvryDtls = value if value is not None else base_types.UninitialisedField(self, 'PhysDlvryDtls', DeliveryParameters3, False)

	@PhysDlvryDtls.deleter
	def PhysDlvryDtls(self):
		del self._PhysDlvryDtls
		self._PhysDlvryDtls = base_types.UninitialisedField(self, 'PhysDlvryDtls', DeliveryParameters3, False)

	@property
	def PhysDlvryInd(self):
		return self._PhysDlvryInd

	@PhysDlvryInd.setter
	def PhysDlvryInd(self, value):
		self._PhysDlvryInd = value if value is not None else base_types.UninitialisedField(self, 'PhysDlvryInd', YesNoIndicator, False)

	@PhysDlvryInd.deleter
	def PhysDlvryInd(self):
		del self._PhysDlvryInd
		self._PhysDlvryInd = base_types.UninitialisedField(self, 'PhysDlvryInd', YesNoIndicator, False)

	@property
	def PrtlRedWhldgAmt(self):
		return self._PrtlRedWhldgAmt

	@PrtlRedWhldgAmt.setter
	def PrtlRedWhldgAmt(self, value):
		self._PrtlRedWhldgAmt = value if value is not None else base_types.UninitialisedField(self, 'PrtlRedWhldgAmt', ActiveCurrencyAndAmount, False)

	@PrtlRedWhldgAmt.deleter
	def PrtlRedWhldgAmt(self):
		del self._PrtlRedWhldgAmt
		self._PrtlRedWhldgAmt = base_types.UninitialisedField(self, 'PrtlRedWhldgAmt', ActiveCurrencyAndAmount, False)

	@property
	def PrtlSttlmOfCsh(self):
		return self._PrtlSttlmOfCsh

	@PrtlSttlmOfCsh.setter
	def PrtlSttlmOfCsh(self, value):
		self._PrtlSttlmOfCsh = value if value is not None else base_types.UninitialisedField(self, 'PrtlSttlmOfCsh', PercentageRate, False)

	@PrtlSttlmOfCsh.deleter
	def PrtlSttlmOfCsh(self):
		del self._PrtlSttlmOfCsh
		self._PrtlSttlmOfCsh = base_types.UninitialisedField(self, 'PrtlSttlmOfCsh', PercentageRate, False)

	@property
	def PrtlSttlmOfUnits(self):
		return self._PrtlSttlmOfUnits

	@PrtlSttlmOfUnits.setter
	def PrtlSttlmOfUnits(self, value):
		self._PrtlSttlmOfUnits = value if value is not None else base_types.UninitialisedField(self, 'PrtlSttlmOfUnits', PercentageRate, False)

	@PrtlSttlmOfUnits.deleter
	def PrtlSttlmOfUnits(self):
		del self._PrtlSttlmOfUnits
		self._PrtlSttlmOfUnits = base_types.UninitialisedField(self, 'PrtlSttlmOfUnits', PercentageRate, False)

	@property
	def PrtlyExctdInd(self):
		return self._PrtlyExctdInd

	@PrtlyExctdInd.setter
	def PrtlyExctdInd(self, value):
		self._PrtlyExctdInd = value if value is not None else base_types.UninitialisedField(self, 'PrtlyExctdInd', YesNoIndicator, False)

	@PrtlyExctdInd.deleter
	def PrtlyExctdInd(self):
		del self._PrtlyExctdInd
		self._PrtlyExctdInd = base_types.UninitialisedField(self, 'PrtlyExctdInd', YesNoIndicator, False)

	@property
	def RltdPtyDtls(self):
		return self._RltdPtyDtls

	@RltdPtyDtls.setter
	def RltdPtyDtls(self, value):
		self._RltdPtyDtls = value if value is not None else base_types.UninitialisedField(self, 'RltdPtyDtls', Intermediary49, True)

	@RltdPtyDtls.deleter
	def RltdPtyDtls(self):
		del self._RltdPtyDtls
		self._RltdPtyDtls = base_types.UninitialisedField(self, 'RltdPtyDtls', Intermediary49, True)

	@property
	def Rndg(self):
		return self._Rndg

	@Rndg.setter
	def Rndg(self, value):
		self._Rndg = value if value is not None else base_types.UninitialisedField(self, 'Rndg', RoundingDirection2Code, False)

	@Rndg.deleter
	def Rndg(self):
		del self._Rndg
		self._Rndg = base_types.UninitialisedField(self, 'Rndg', RoundingDirection2Code, False)

	@property
	def SgntrTp(self):
		return self._SgntrTp

	@SgntrTp.setter
	def SgntrTp(self, value):
		self._SgntrTp = value if value is not None else base_types.UninitialisedField(self, 'SgntrTp', SignatureType1Choice, False)

	@SgntrTp.deleter
	def SgntrTp(self):
		del self._SgntrTp
		self._SgntrTp = base_types.UninitialisedField(self, 'SgntrTp', SignatureType1Choice, False)

	@property
	def StffClntBrkdwn(self):
		return self._StffClntBrkdwn

	@StffClntBrkdwn.setter
	def StffClntBrkdwn(self, value):
		self._StffClntBrkdwn = value if value is not None else base_types.UninitialisedField(self, 'StffClntBrkdwn', InvestmentFundsOrderBreakdown2, True)

	@StffClntBrkdwn.deleter
	def StffClntBrkdwn(self):
		del self._StffClntBrkdwn
		self._StffClntBrkdwn = base_types.UninitialisedField(self, 'StffClntBrkdwn', InvestmentFundsOrderBreakdown2, True)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', ActiveCurrencyAndAmount, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', ActiveCurrencyAndAmount, False)

	@property
	def SttlmAndCtdyDtls(self):
		return self._SttlmAndCtdyDtls

	@SttlmAndCtdyDtls.setter
	def SttlmAndCtdyDtls(self, value):
		self._SttlmAndCtdyDtls = value if value is not None else base_types.UninitialisedField(self, 'SttlmAndCtdyDtls', FundSettlementParameters22, False)

	@SttlmAndCtdyDtls.deleter
	def SttlmAndCtdyDtls(self):
		del self._SttlmAndCtdyDtls
		self._SttlmAndCtdyDtls = base_types.UninitialisedField(self, 'SttlmAndCtdyDtls', FundSettlementParameters22, False)

	@property
	def SttlmMtd(self):
		return self._SttlmMtd

	@SttlmMtd.setter
	def SttlmMtd(self, value):
		self._SttlmMtd = value if value is not None else base_types.UninitialisedField(self, 'SttlmMtd', DeliveryReceiptType2Code, False)

	@SttlmMtd.deleter
	def SttlmMtd(self):
		del self._SttlmMtd
		self._SttlmMtd = base_types.UninitialisedField(self, 'SttlmMtd', DeliveryReceiptType2Code, False)

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if value is not None else base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTime2Choice, False)

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTime2Choice, False)

	@property
	def TxChanlTp(self):
		return self._TxChanlTp

	@TxChanlTp.setter
	def TxChanlTp(self, value):
		self._TxChanlTp = value if value is not None else base_types.UninitialisedField(self, 'TxChanlTp', TransactionChannelType1Choice, False)

	@TxChanlTp.deleter
	def TxChanlTp(self):
		del self._TxChanlTp
		self._TxChanlTp = base_types.UninitialisedField(self, 'TxChanlTp', TransactionChannelType1Choice, False)

	@property
	def TxOvrhd(self):
		return self._TxOvrhd

	@TxOvrhd.setter
	def TxOvrhd(self, value):
		self._TxOvrhd = value if value is not None else base_types.UninitialisedField(self, 'TxOvrhd', TotalFeesAndTaxes45, False)

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = base_types.UninitialisedField(self, 'TxOvrhd', TotalFeesAndTaxes45, False)

	@property
	def Units(self):
		return self._Units

	@Units.setter
	def Units(self, value):
		self._Units = value if value is not None else base_types.UninitialisedField(self, 'Units', Unit1Choice, False)

	@Units.deleter
	def Units(self):
		del self._Units
		self._Units = base_types.UninitialisedField(self, 'Units', Unit1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BestExctn', type=BestExecution1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=IndividualPerson32, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=PaymentTransaction167, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealgPricDtls', type=UnitPrice22, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlAsstSttlm', type=DigitalPaymentSettlement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinAdvc', type=FinancialAdvice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp1Or2Units', type=UKTaxGroupUnit1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GtgOrHldBckDtls', type=HoldBackInformation5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgsRedRate', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InftvPricDtls', type=UnitPrice22, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='InftvTaxDtls', type=InformativeTax2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmPrftAmt', type=ProfitAndLoss2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LateRpt', type=LateReport1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgtdTrad', type=NegotiatedTrade1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=FundOrderType4Choice, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrWvrDtls', type=OrderWaiver1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryDtls', type=DeliveryParameters3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlRedWhldgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmOfCsh', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlmOfUnits', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlyExctdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPtyDtls', type=Intermediary49, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StffClntBrkdwn', type=InvestmentFundsOrderBreakdown2, min=0, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=TotalFeesAndTaxes45, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Units', type=Unit1Choice, min=1, max=1, mutex_group=None, array=False),
	))