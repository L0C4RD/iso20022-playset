from . import base_types
from ._NegotiatedTrade1Code import NegotiatedTrade1Code
from ._OrderWaiver1 import OrderWaiver1
from ._InvestmentAccount58 import InvestmentAccount58
from ._NameAndAddress4 import NameAndAddress4
from ._SourceOfCash1Choice import SourceOfCash1Choice
from ._IncomePreference1Code import IncomePreference1Code
from ._FinancialAdvice1Code import FinancialAdvice1Code
from ._Intermediary40 import Intermediary40
from ._YesNoIndicator import YesNoIndicator
from ._SignatureType1Choice import SignatureType1Choice
from ._FundOrderType4Choice import FundOrderType4Choice
from ._InvestmentFundsOrderBreakdown2 import InvestmentFundsOrderBreakdown2
from ._ISODate import ISODate
from ._PaymentTransaction70 import PaymentTransaction70
from ._TransactionChannelType1Choice import TransactionChannelType1Choice
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max350Text import Max350Text
from ._Equalisation1 import Equalisation1
from ._FundSettlementParameters11 import FundSettlementParameters11
from ._CustomerConductClassification1Choice import CustomerConductClassification1Choice
from ._DeliveryReceiptType2Code import DeliveryReceiptType2Code
from ._IndividualPerson31 import IndividualPerson31
from ._FeeAndTax1 import FeeAndTax1
from ._Max35Text import Max35Text
from ._RoundingDirection2Code import RoundingDirection2Code
from ._ForeignExchangeTerms32 import ForeignExchangeTerms32
from ._FinancialInstrumentQuantity27Choice import FinancialInstrumentQuantity27Choice

class SubscriptionOrder15(base_types._BaseFieldType):

	__slots__ = ["_CstmrCndctClssfctn", "_FXDtls", "_SttlmMtd", "_NonStdSttlmInf", "_OrdrTp", "_InvstmtAcctDtls", "_Rndg", "_AmtOrUnits", "_TxChanlTp", "_CshSttlmDtls", "_NgtdTrad", "_TxOvrhd", "_CshSttlmDt", "_PhysDlvryInd", "_RltdPtyDtls", "_StffClntBrkdwn", "_SttlmAndCtdyDtls", "_BnfcryDtls", "_IncmPref", "_LttrInttRef", "_ClntRef", "_PhysDlvryDtls", "_OrdrRef", "_AcmltnRghtRef", "_FinAdvc", "_SgntrTp", "_OrdrWvrDtls", "_SttlmAmt", "_Equlstn", "_SrcOfCsh"]
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
	def AmtOrUnits(self):
		return self._AmtOrUnits

	@AmtOrUnits.setter
	def AmtOrUnits(self, value):
		self._AmtOrUnits = value if type(value) != base_types.auto else self.make_default("AmtOrUnits")

	@AmtOrUnits.deleter
	def AmtOrUnits(self):
		del self._AmtOrUnits
		self._AmtOrUnits = None

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
	def LttrInttRef(self):
		return self._LttrInttRef

	@LttrInttRef.setter
	def LttrInttRef(self, value):
		self._LttrInttRef = value if type(value) != base_types.auto else self.make_default("LttrInttRef")

	@LttrInttRef.deleter
	def LttrInttRef(self):
		del self._LttrInttRef
		self._LttrInttRef = None

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
	def AcmltnRghtRef(self):
		return self._AcmltnRghtRef

	@AcmltnRghtRef.setter
	def AcmltnRghtRef(self, value):
		self._AcmltnRghtRef = value if type(value) != base_types.auto else self.make_default("AcmltnRghtRef")

	@AcmltnRghtRef.deleter
	def AcmltnRghtRef(self):
		del self._AcmltnRghtRef
		self._AcmltnRghtRef = None

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
	def SrcOfCsh(self):
		return self._SrcOfCsh

	@SrcOfCsh.setter
	def SrcOfCsh(self, value):
		self._SrcOfCsh = value if type(value) != base_types.auto else self.make_default("SrcOfCsh")

	@SrcOfCsh.deleter
	def SrcOfCsh(self):
		del self._SrcOfCsh
		self._SrcOfCsh = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonStdSttlmInf', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrTp', type=FundOrderType4Choice, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rndg', type=RoundingDirection2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtOrUnits', type=FinancialInstrumentQuantity27Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=PaymentTransaction70, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgtdTrad', type=NegotiatedTrade1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOvrhd', type=FeeAndTax1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPtyDtls', type=Intermediary40, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='StffClntBrkdwn', type=InvestmentFundsOrderBreakdown2, min=0, max=4, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAndCtdyDtls', type=FundSettlementParameters11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryDtls', type=IndividualPerson31, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IncmPref', type=IncomePreference1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LttrInttRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PhysDlvryDtls', type=NameAndAddress4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcmltnRghtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinAdvc', type=FinancialAdvice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrWvrDtls', type=OrderWaiver1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Equlstn', type=Equalisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfCsh', type=SourceOfCash1Choice, min=0, max=None, mutex_group=None, array=True),
	))

