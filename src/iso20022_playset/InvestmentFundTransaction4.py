import base_types
import ReversalCode
import DateAndDateTimeChoice
import UnitPrice20
import TransactionStatus1Code
import YesNoIndicator
import ISODateTime
import Max35Text
import TransactionType1Choice
import FinancialInstrumentQuantity1
import ActiveCurrencyAndAmount
import ISODate
import CreditDebitCode

class InvestmentFundTransaction4(base_types._BaseFieldType):

	__slots__ = ["_OrdrRef", "_DealRef", "_TradDtTm", "_SttldTxInd", "_UnitsQty", "_RegdTxInd", "_SttlmDt", "_SttlmAmt", "_CdtDbt", "_Rvsl", "_MstrRef", "_BookgSts", "_ClntRef", "_OrdrDtTm", "_EvtTp", "_PricDtls", "_LegExctnId", "_LegId", "_CumDvddInd", "_PrtlyExctdInd"]
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
	def DealRef(self):
		return self._DealRef

	@DealRef.setter
	def DealRef(self, value):
		self._DealRef = value if type(value) != auto else self.make_default("DealRef")

	@DealRef.deleter
	def DealRef(self):
		del self._DealRef
		self._DealRef = None

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
	def SttldTxInd(self):
		return self._SttldTxInd

	@SttldTxInd.setter
	def SttldTxInd(self, value):
		self._SttldTxInd = value if type(value) != auto else self.make_default("SttldTxInd")

	@SttldTxInd.deleter
	def SttldTxInd(self):
		del self._SttldTxInd
		self._SttldTxInd = None

	@property
	def UnitsQty(self):
		return self._UnitsQty

	@UnitsQty.setter
	def UnitsQty(self, value):
		self._UnitsQty = value if type(value) != auto else self.make_default("UnitsQty")

	@UnitsQty.deleter
	def UnitsQty(self):
		del self._UnitsQty
		self._UnitsQty = None

	@property
	def RegdTxInd(self):
		return self._RegdTxInd

	@RegdTxInd.setter
	def RegdTxInd(self, value):
		self._RegdTxInd = value if type(value) != auto else self.make_default("RegdTxInd")

	@RegdTxInd.deleter
	def RegdTxInd(self):
		del self._RegdTxInd
		self._RegdTxInd = None

	@property
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if type(value) != auto else self.make_default("SttlmDt")

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = None

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
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def Rvsl(self):
		return self._Rvsl

	@Rvsl.setter
	def Rvsl(self, value):
		self._Rvsl = value if type(value) != auto else self.make_default("Rvsl")

	@Rvsl.deleter
	def Rvsl(self):
		del self._Rvsl
		self._Rvsl = None

	@property
	def MstrRef(self):
		return self._MstrRef

	@MstrRef.setter
	def MstrRef(self, value):
		self._MstrRef = value if type(value) != auto else self.make_default("MstrRef")

	@MstrRef.deleter
	def MstrRef(self):
		del self._MstrRef
		self._MstrRef = None

	@property
	def BookgSts(self):
		return self._BookgSts

	@BookgSts.setter
	def BookgSts(self, value):
		self._BookgSts = value if type(value) != auto else self.make_default("BookgSts")

	@BookgSts.deleter
	def BookgSts(self):
		del self._BookgSts
		self._BookgSts = None

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
	def OrdrDtTm(self):
		return self._OrdrDtTm

	@OrdrDtTm.setter
	def OrdrDtTm(self, value):
		self._OrdrDtTm = value if type(value) != auto else self.make_default("OrdrDtTm")

	@OrdrDtTm.deleter
	def OrdrDtTm(self):
		del self._OrdrDtTm
		self._OrdrDtTm = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if type(value) != auto else self.make_default("PricDtls")

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = None

	@property
	def LegExctnId(self):
		return self._LegExctnId

	@LegExctnId.setter
	def LegExctnId(self, value):
		self._LegExctnId = value if type(value) != auto else self.make_default("LegExctnId")

	@LegExctnId.deleter
	def LegExctnId(self):
		del self._LegExctnId
		self._LegExctnId = None

	@property
	def LegId(self):
		return self._LegId

	@LegId.setter
	def LegId(self, value):
		self._LegId = value if type(value) != auto else self.make_default("LegId")

	@LegId.deleter
	def LegId(self):
		del self._LegId
		self._LegId = None

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
	def PrtlyExctdInd(self):
		return self._PrtlyExctdInd

	@PrtlyExctdInd.setter
	def PrtlyExctdInd(self, value):
		self._PrtlyExctdInd = value if type(value) != auto else self.make_default("PrtlyExctdInd")

	@PrtlyExctdInd.deleter
	def PrtlyExctdInd(self):
		del self._PrtlyExctdInd
		self._PrtlyExctdInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldTxInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsQty', type=FinancialInstrumentQuantity1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdTxInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvsl', type=ReversalCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookgSts', type=TransactionStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=TransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegExctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlyExctdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

