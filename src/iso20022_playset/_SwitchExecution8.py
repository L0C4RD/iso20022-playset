# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AdditionalAmount1Choice
from . import BestExecution1Code
from . import CancellationRight1Choice
from . import CustomerConductClassification1Choice
from . import DeliveryReceiptType2Code
from . import FinancialAdvice1Code
from . import ForeignExchangeTerms37
from . import ISODate
from . import ISODateTime
from . import Intermediary49
from . import InvestmentAccount81
from . import LateReport1Code
from . import Max35Text
from . import NegotiatedTrade1Code
from . import OrderWaiver1
from . import PaymentTransaction181
from . import PlaceOfTradeIdentification4Choice
from . import SignatureType1Choice
from . import SwitchRedemptionLegExecution5
from . import SwitchSubscriptionLegExecution5
from . import TransactionChannelType1Choice
from . import YesNoIndicator

class SwitchExecution8(base_types._BaseFieldType):

	__slots__ = ["_AddtlAmt", "_AmdmntInd", "_BestExctn", "_ClntRef", "_CshSttlmDt", "_CshSttlmDtls", "_CstmrCndctClssfctn", "_CxlRght", "_DealRef", "_FXDtls", "_FinAdvc", "_InvstmtAcctDtls", "_LateRpt", "_MstrRef", "_NgtdTrad", "_NonceId", "_OrdrDtTm", "_OrdrRef", "_OrdrWvrDtls", "_PlcOfTrad", "_RcvdDtTm", "_RedLegDtls", "_ReqdFutrTradDt", "_RltdPtyDtls", "_SbcptLegDtls", "_SgntrTp", "_SttlmAmt", "_SttlmMtd", "_TxChanlTp"]
	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if value is not None else base_types.UninitialisedField(self, 'AddtlAmt', AdditionalAmount1Choice, False)

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = base_types.UninitialisedField(self, 'AddtlAmt', AdditionalAmount1Choice, False)

	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if value is not None else base_types.UninitialisedField(self, 'AmdmntInd', YesNoIndicator, False)

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = base_types.UninitialisedField(self, 'AmdmntInd', YesNoIndicator, False)

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
		self._CshSttlmDtls = value if value is not None else base_types.UninitialisedField(self, 'CshSttlmDtls', PaymentTransaction181, False)

	@CshSttlmDtls.deleter
	def CshSttlmDtls(self):
		del self._CshSttlmDtls
		self._CshSttlmDtls = base_types.UninitialisedField(self, 'CshSttlmDtls', PaymentTransaction181, False)

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
	def CxlRght(self):
		return self._CxlRght

	@CxlRght.setter
	def CxlRght(self, value):
		self._CxlRght = value if value is not None else base_types.UninitialisedField(self, 'CxlRght', CancellationRight1Choice, False)

	@CxlRght.deleter
	def CxlRght(self):
		del self._CxlRght
		self._CxlRght = base_types.UninitialisedField(self, 'CxlRght', CancellationRight1Choice, False)

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
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if value is not None else base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = base_types.UninitialisedField(self, 'MstrRef', Max35Text, False)

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
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if value is not None else base_types.UninitialisedField(self, 'OrdrDtTm', ISODateTime, False)

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = base_types.UninitialisedField(self, 'OrdrDtTm', ISODateTime, False)

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
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if value is not None else base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification4Choice, False)

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = base_types.UninitialisedField(self, 'PlcOfTrad', PlaceOfTradeIdentification4Choice, False)

	@property
	def RcvdDtTm(self):
		return self._RcvdDtTm

	@RcvdDtTm.setter
	def RcvdDtTm(self, value):
		self._RcvdDtTm = value if value is not None else base_types.UninitialisedField(self, 'RcvdDtTm', ISODateTime, False)

	@RcvdDtTm.deleter
	def RcvdDtTm(self):
		del self._RcvdDtTm
		self._RcvdDtTm = base_types.UninitialisedField(self, 'RcvdDtTm', ISODateTime, False)

	@property
	def RedLegDtls(self):
		return self._RedLegDtls

	@RedLegDtls.setter
	def RedLegDtls(self, value):
		self._RedLegDtls = value if value is not None else base_types.UninitialisedField(self, 'RedLegDtls', SwitchRedemptionLegExecution5, True)

	@RedLegDtls.deleter
	def RedLegDtls(self):
		del self._RedLegDtls
		self._RedLegDtls = base_types.UninitialisedField(self, 'RedLegDtls', SwitchRedemptionLegExecution5, True)

	@property
	def ReqdFutrTradDt(self):
		return self._ReqdFutrTradDt

	@ReqdFutrTradDt.setter
	def ReqdFutrTradDt(self, value):
		self._ReqdFutrTradDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdFutrTradDt', ISODate, False)

	@ReqdFutrTradDt.deleter
	def ReqdFutrTradDt(self):
		del self._ReqdFutrTradDt
		self._ReqdFutrTradDt = base_types.UninitialisedField(self, 'ReqdFutrTradDt', ISODate, False)

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
	def SbcptLegDtls(self):
		return self._SbcptLegDtls

	@SbcptLegDtls.setter
	def SbcptLegDtls(self, value):
		self._SbcptLegDtls = value if value is not None else base_types.UninitialisedField(self, 'SbcptLegDtls', SwitchSubscriptionLegExecution5, True)

	@SbcptLegDtls.deleter
	def SbcptLegDtls(self):
		del self._SbcptLegDtls
		self._SbcptLegDtls = base_types.UninitialisedField(self, 'SbcptLegDtls', SwitchSubscriptionLegExecution5, True)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAmt', type=AdditionalAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BestExctn', type=BestExecution1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=PaymentTransaction181, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRght', type=CancellationRight1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms37, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinAdvc', type=FinancialAdvice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount81, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LateRpt', type=LateReport1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NgtdTrad', type=NegotiatedTrade1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonceId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrWvrDtls', type=OrderWaiver1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvdDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedLegDtls', type=SwitchRedemptionLegExecution5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdFutrTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPtyDtls', type=Intermediary49, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbcptLegDtls', type=SwitchSubscriptionLegExecution5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
	))