from . import base_types
from .DateAndDateTimeChoice import DateAndDateTimeChoice
from .OrderWaiver1 import OrderWaiver1
from .SwitchRedemptionLegOrder6 import SwitchRedemptionLegOrder6
from .CustomerConductClassification1Choice import CustomerConductClassification1Choice
from .FinancialAdvice1Code import FinancialAdvice1Code
from .TransactionChannelType1Choice import TransactionChannelType1Choice
from .ISODate import ISODate
from .InvestmentAccount58 import InvestmentAccount58
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .SwitchSubscriptionLegOrder6 import SwitchSubscriptionLegOrder6
from .ForeignExchangeTerms32 import ForeignExchangeTerms32
from .ISODateTime import ISODateTime
from .CancellationRight1Choice import CancellationRight1Choice
from .DeliveryReceiptType2Code import DeliveryReceiptType2Code
from .AdditionalAmount1Choice import AdditionalAmount1Choice
from .Max35Text import Max35Text
from .SignatureType1Choice import SignatureType1Choice
from .PaymentTransaction71 import PaymentTransaction71
from .NegotiatedTrade1Code import NegotiatedTrade1Code
from .Intermediary40 import Intermediary40
from .PlaceOfTradeIdentification1Choice import PlaceOfTradeIdentification1Choice

class SwitchOrder7(base_types._BaseFieldType):

	__slots__ = ["_AddtlAmt", "_SbcptLegDtls", "_NgtdTrad", "_XpryDtTm", "_PlcOfTrad", "_ReqdFutrTradDt", "_SttlmMtd", "_OrdrRef", "_CshSttlmDtls", "_RedLegDtls", "_InvstmtAcctDtls", "_CstmrCndctClssfctn", "_FinAdvc", "_ClntRef", "_MstrRef", "_FXDtls", "_OrdrDtTm", "_OrdrWvrDtls", "_CxlRght", "_CshSttlmDt", "_TxChanlTp", "_SgntrTp", "_RltdPtyDtls", "_SttlmAmt"]
	@property
	def AddtlAmt(self):
		return self._AddtlAmt

	@AddtlAmt.setter
	def AddtlAmt(self, value):
		self._AddtlAmt = value if type(value) != base_types.auto else self.make_default("AddtlAmt")

	@AddtlAmt.deleter
	def AddtlAmt(self):
		del self._AddtlAmt
		self._AddtlAmt = None

	@property
	def SbcptLegDtls(self):
		return self._SbcptLegDtls

	@SbcptLegDtls.setter
	def SbcptLegDtls(self, value):
		self._SbcptLegDtls = value if type(value) != base_types.auto else self.make_default("SbcptLegDtls")

	@SbcptLegDtls.deleter
	def SbcptLegDtls(self):
		del self._SbcptLegDtls
		self._SbcptLegDtls = None

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
	def XpryDtTm(self):
		return self._XpryDtTm

	@XpryDtTm.setter
	def XpryDtTm(self, value):
		self._XpryDtTm = value if type(value) != base_types.auto else self.make_default("XpryDtTm")

	@XpryDtTm.deleter
	def XpryDtTm(self):
		del self._XpryDtTm
		self._XpryDtTm = None

	@property
	def PlcOfTrad(self):
		return self._PlcOfTrad

	@PlcOfTrad.setter
	def PlcOfTrad(self, value):
		self._PlcOfTrad = value if type(value) != base_types.auto else self.make_default("PlcOfTrad")

	@PlcOfTrad.deleter
	def PlcOfTrad(self):
		del self._PlcOfTrad
		self._PlcOfTrad = None

	@property
	def ReqdFutrTradDt(self):
		return self._ReqdFutrTradDt

	@ReqdFutrTradDt.setter
	def ReqdFutrTradDt(self, value):
		self._ReqdFutrTradDt = value if type(value) != base_types.auto else self.make_default("ReqdFutrTradDt")

	@ReqdFutrTradDt.deleter
	def ReqdFutrTradDt(self):
		del self._ReqdFutrTradDt
		self._ReqdFutrTradDt = None

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
	def RedLegDtls(self):
		return self._RedLegDtls

	@RedLegDtls.setter
	def RedLegDtls(self, value):
		self._RedLegDtls = value if type(value) != base_types.auto else self.make_default("RedLegDtls")

	@RedLegDtls.deleter
	def RedLegDtls(self):
		del self._RedLegDtls
		self._RedLegDtls = None

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
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != base_types.auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

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
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if type(value) != base_types.auto else self.make_default("OrdrDtTm")

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = None

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
	def CxlRght(self):
		return self._CxlRght

	@CxlRght.setter
	def CxlRght(self, value):
		self._CxlRght = value if type(value) != base_types.auto else self.make_default("CxlRght")

	@CxlRght.deleter
	def CxlRght(self):
		del self._CxlRght
		self._CxlRght = None

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
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlAmt', type=AdditionalAmount1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbcptLegDtls', type=SwitchSubscriptionLegOrder6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NgtdTrad', type=NegotiatedTrade1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpryDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlcOfTrad', type=PlaceOfTradeIdentification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdFutrTradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmMtd', type=DeliveryReceiptType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDtls', type=PaymentTransaction71, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RedLegDtls', type=SwitchRedemptionLegOrder6, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrCndctClssfctn', type=CustomerConductClassification1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinAdvc', type=FinancialAdvice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms32, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrWvrDtls', type=OrderWaiver1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlRght', type=CancellationRight1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxChanlTp', type=TransactionChannelType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SgntrTp', type=SignatureType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdPtyDtls', type=Intermediary40, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

