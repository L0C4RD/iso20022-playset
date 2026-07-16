# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CreditDebitCode
from . import DateAndDateTimeChoice
from . import FinancialInstrumentQuantity1
from . import ISODate
from . import ISODateTime
from . import Max35Text
from . import ReversalCode
from . import TransactionStatus1Code
from . import TransactionType1Choice
from . import UnitPrice20
from . import YesNoIndicator

class InvestmentFundTransaction4(base_types._BaseFieldType):

	__slots__ = ["_BookgSts", "_CdtDbt", "_ClntRef", "_CumDvddInd", "_DealRef", "_EvtTp", "_LegExctnId", "_LegId", "_MstrRef", "_OrdrDtTm", "_OrdrRef", "_PricDtls", "_PrtlyExctdInd", "_RegdTxInd", "_Rvsl", "_SttldTxInd", "_SttlmAmt", "_SttlmDt", "_TradDtTm", "_UnitsQty"]
	@property
	def BookgSts(self):
		return self._BookgSts

	@BookgSts.setter
	def BookgSts(self, value):
		self._BookgSts = value if value is not None else base_types.UninitialisedField(self, 'BookgSts', TransactionStatus1Code, False)

	@BookgSts.deleter
	def BookgSts(self):
		del self._BookgSts
		self._BookgSts = base_types.UninitialisedField(self, 'BookgSts', TransactionStatus1Code, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebitCode, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebitCode, False)

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
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', TransactionType1Choice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', TransactionType1Choice, False)

	@property
	def LegExctnId(self):
		return self._LegExctnId

	@LegExctnId.setter
	def LegExctnId(self, value):
		self._LegExctnId = value if value is not None else base_types.UninitialisedField(self, 'LegExctnId', Max35Text, False)

	@LegExctnId.deleter
	def LegExctnId(self):
		del self._LegExctnId
		self._LegExctnId = base_types.UninitialisedField(self, 'LegExctnId', Max35Text, False)

	@property
	def LegId(self):
		return self._LegId

	@LegId.setter
	def LegId(self, value):
		self._LegId = value if value is not None else base_types.UninitialisedField(self, 'LegId', Max35Text, False)

	@LegId.deleter
	def LegId(self):
		del self._LegId
		self._LegId = base_types.UninitialisedField(self, 'LegId', Max35Text, False)

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
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', UnitPrice20, False)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', UnitPrice20, False)

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
	def RegdTxInd(self):
		return self._RegdTxInd

	@RegdTxInd.setter
	def RegdTxInd(self, value):
		self._RegdTxInd = value if value is not None else base_types.UninitialisedField(self, 'RegdTxInd', YesNoIndicator, False)

	@RegdTxInd.deleter
	def RegdTxInd(self):
		del self._RegdTxInd
		self._RegdTxInd = base_types.UninitialisedField(self, 'RegdTxInd', YesNoIndicator, False)

	@property
	def Rvsl(self):
		return self._Rvsl

	@Rvsl.setter
	def Rvsl(self, value):
		self._Rvsl = value if value is not None else base_types.UninitialisedField(self, 'Rvsl', ReversalCode, False)

	@Rvsl.deleter
	def Rvsl(self):
		del self._Rvsl
		self._Rvsl = base_types.UninitialisedField(self, 'Rvsl', ReversalCode, False)

	@property
	def SttldTxInd(self):
		return self._SttldTxInd

	@SttldTxInd.setter
	def SttldTxInd(self, value):
		self._SttldTxInd = value if value is not None else base_types.UninitialisedField(self, 'SttldTxInd', YesNoIndicator, False)

	@SttldTxInd.deleter
	def SttldTxInd(self):
		del self._SttldTxInd
		self._SttldTxInd = base_types.UninitialisedField(self, 'SttldTxInd', YesNoIndicator, False)

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
	def SttlmDt(self):
		return self._SttlmDt

	@SttlmDt.setter
	def SttlmDt(self, value):
		self._SttlmDt = value if value is not None else base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@SttlmDt.deleter
	def SttlmDt(self):
		del self._SttlmDt
		self._SttlmDt = base_types.UninitialisedField(self, 'SttlmDt', ISODate, False)

	@property
	def TradDtTm(self):
		return self._TradDtTm

	@TradDtTm.setter
	def TradDtTm(self, value):
		self._TradDtTm = value if value is not None else base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTimeChoice, False)

	@TradDtTm.deleter
	def TradDtTm(self):
		del self._TradDtTm
		self._TradDtTm = base_types.UninitialisedField(self, 'TradDtTm', DateAndDateTimeChoice, False)

	@property
	def UnitsQty(self):
		return self._UnitsQty

	@UnitsQty.setter
	def UnitsQty(self, value):
		self._UnitsQty = value if value is not None else base_types.UninitialisedField(self, 'UnitsQty', FinancialInstrumentQuantity1, False)

	@UnitsQty.deleter
	def UnitsQty(self):
		del self._UnitsQty
		self._UnitsQty = base_types.UninitialisedField(self, 'UnitsQty', FinancialInstrumentQuantity1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BookgSts', type=TransactionStatus1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebitCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClntRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CumDvddInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DealRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=TransactionType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegExctnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MstrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=UnitPrice20, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlyExctdInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegdTxInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rvsl', type=ReversalCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldTxInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDtTm', type=DateAndDateTimeChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitsQty', type=FinancialInstrumentQuantity1, min=1, max=1, mutex_group=None, array=False),
	))