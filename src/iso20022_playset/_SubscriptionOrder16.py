# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CustomerConductClassification1Choice
from . import DeliveryReceiptType2Code
from . import DigitalPaymentSettlement3
from . import Equalisation1
from . import FeeAndTax2
from . import FinancialAdvice1Code
from . import FinancialInstrumentQuantity49Choice
from . import ForeignExchangeTerms44
from . import FundOrderType4Choice
from . import FundSettlementParameters22
from . import ISODate
from . import IncomePreference1Code
from . import IndividualPerson31
from . import Intermediary49
from . import InvestmentAccount81
from . import InvestmentFundsOrderBreakdown2
from . import Max350Text
from . import Max35Text
from . import NameAndAddress4
from . import NegotiatedTrade1Code
from . import OrderWaiver1
from . import PaymentTransaction180
from . import RoundingDirection2Code
from . import SignatureType1Choice
from . import SourceOfCash1Choice
from . import TransactionChannelType1Choice
from . import YesNoIndicator

class SubscriptionOrder16(base_types._BaseFieldType):

	__slots__ = ["_AcmltnRghtRef", "_AmtOrUnits", "_BnfcryDtls", "_ClntRef", "_CshSttlmDt", "_CshSttlmDtls", "_CstmrCndctClssfctn", "_DgtlAsstSttlm", "_Equlstn", "_FXDtls", "_FinAdvc", "_IncmPref", "_InvstmtAcctDtls", "_LttrInttRef", "_NgtdTrad", "_NonStdSttlmInf", "_NonceId", "_OrdrRef", "_OrdrTp", "_OrdrWvrDtls", "_PhysDlvryDtls", "_PhysDlvryInd", "_RltdPtyDtls", "_Rndg", "_SgntrTp", "_SrcOfCsh", "_StffClntBrkdwn", "_SttlmAmt", "_SttlmAndCtdyDtls", "_SttlmMtd", "_TxChanlTp", "_TxOvrhd"]
	@property
	def AcmltnRghtRef(self):
		return self._AcmltnRghtRef

	@AcmltnRghtRef.setter
	def AcmltnRghtRef(self, value):
		self._AcmltnRghtRef = value if value is not None else base_types.UninitialisedField(self, 'AcmltnRghtRef', Max35Text, False)

	@AcmltnRghtRef.deleter
	def AcmltnRghtRef(self):
		del self._AcmltnRghtRef
		self._AcmltnRghtRef = base_types.UninitialisedField(self, 'AcmltnRghtRef', Max35Text, False)

	@property
	def AmtOrUnits(self):
		return self._AmtOrUnits

	@AmtOrUnits.setter
	def AmtOrUnits(self, value):
		self._AmtOrUnits = value if value is not None else base_types.UninitialisedField(self, 'AmtOrUnits', FinancialInstrumentQuantity49Choice, False)

	@AmtOrUnits.deleter
	def AmtOrUnits(self):
		del self._AmtOrUnits
		self._AmtOrUnits = base_types.UninitialisedField(self, 'AmtOrUnits', FinancialInstrumentQuantity49Choice, False)

	@property
	def BnfcryDtls(self):
		return self._BnfcryDtls

	@BnfcryDtls.setter
	def BnfcryDtls(self, value):
		self._BnfcryDtls = value if value is not None else base_types.UninitialisedField(self, 'BnfcryDtls', IndividualPerson31, True)

	@BnfcryDtls.deleter
	def BnfcryDtls(self):
		del self._BnfcryDtls
		self._BnfcryDtls = base_types.UninitialisedField(self, 'BnfcryDtls', IndividualPerson31, True)

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
		self._CshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDtls', PaymentTransaction180, False)

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = base_types.UninitialisedField(self, 'CshSttlmDtls', PaymentTransaction180, False)

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
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms44, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms44, False)

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
	def LttrInttRef(self):
		return self._LttrInttRef

	@LttrInttRef.setter
	def LttrInttRef(self, value):
		self._LttrInttRef = value if value is not None else base_types.UninitialisedField(self, 'LttrInttRef', Max35Text, False)

	@LttrInttRef.deleter
	def LttrInttRef(self):
		del self._LttrInttRef
		self._LttrInttRef = base_types.UninitialisedField(self, 'LttrInttRef', Max35Text, False)

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
		self._PhysDlvryDtls = value if value is not None else base_types.UninitialisedField(self, 'PhysDlvryDtls', NameAndAddress4, False)

	@PhysDlvryDtls.deleter
	def PhysDlvryDtls(self):
		del self._PhysDlvryDtls
		self._PhysDlvryDtls = base_types.UninitialisedField(self, 'PhysDlvryDtls', NameAndAddress4, False)

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
	def SrcOfCsh(self):
		return self._SrcOfCsh

	@SrcOfCsh.setter
	def SrcOfCsh(self, value):
		self._SrcOfCsh = value if value is not None else base_types.UninitialisedField(self, 'SrcOfCsh', SourceOfCash1Choice, True)

	@SrcOfCsh.deleter
	def SrcOfCsh(self):
		del self._SrcOfCsh
		self._SrcOfCsh = base_types.UninitialisedField(self, 'SrcOfCsh', SourceOfCash1Choice, True)

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
		self._TxOvrhd = value if value is not None else base_types.UninitialisedField(self, 'TxOvrhd', FeeAndTax2, False)

	@TxOvrhd.deleter
	def TxOvrhd(self):
		del self._TxOvrhd
		self._TxOvrhd = base_types.UninitialisedField(self, 'TxOvrhd', FeeAndTax2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcmltnRghtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtOrUnits', type=FinancialInstrumentQuantity49Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=IndividualPerson31, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=PaymentTransaction180, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DgtlAsstSttlm', type=DigitalPaymentSettlement3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms44, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinAdvc', type=FinancialAdvice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrInttRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgtdTrad', type=NegotiatedTrade1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=FundOrderType4Choice, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrWvrDtls', type=OrderWaiver1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryDtls', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPtyDtls', type=Intermediary49, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfCsh', type=SourceOfCash1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StffClntBrkdwn', type=InvestmentFundsOrderBreakdown2, min=0, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=FeeAndTax2, min=0, max=1, mutex_group=None, array=False),
	))