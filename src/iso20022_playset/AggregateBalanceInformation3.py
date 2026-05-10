from . import base_types
from .SafekeepingPlaceFormatChoice import SafekeepingPlaceFormatChoice
from .ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from .FinancialInstrument13 import FinancialInstrument13
from .AggregateBalancePerSafekeepingPlace4 import AggregateBalancePerSafekeepingPlace4
from .PriceInformation2 import PriceInformation2
from .AdditionalBalanceInformation2 import AdditionalBalanceInformation2
from .Number import Number
from .PlusOrMinusIndicator import PlusOrMinusIndicator
from .BalanceQuantity1Choice import BalanceQuantity1Choice
from .ForeignExchangeTerms6 import ForeignExchangeTerms6
from .SubBalanceInformation2 import SubBalanceInformation2

class AggregateBalanceInformation3(base_types._BaseFieldType):

	__slots__ = ["_BalBrkdwnDtls", "_DaysAcrd", "_AggtQty", "_FXDtls", "_PricDtls", "_AcrdIntrstAmt", "_BookVal", "_HldgVal", "_FinInstrmDtls", "_AddtlBalBrkdwnDtls", "_SfkpgPlc", "_AcrdIntrstAmtSgn", "_BalAtSfkpgPlc", "_PrvsHldgVal"]
	@property
	def BalBrkdwnDtls(self):
		return self._BalBrkdwnDtls

	@BalBrkdwnDtls.setter
	def BalBrkdwnDtls(self, value):
		self._BalBrkdwnDtls = value if type(value) != auto else self.make_default("BalBrkdwnDtls")

	@BalBrkdwnDtls.deleter
	def BalBrkdwnDtls(self):
		del self._BalBrkdwnDtls
		self._BalBrkdwnDtls = None

	@property
	def DaysAcrd(self):
		return self._DaysAcrd

	@DaysAcrd.setter
	def DaysAcrd(self, value):
		self._DaysAcrd = value if type(value) != auto else self.make_default("DaysAcrd")

	@DaysAcrd.deleter
	def DaysAcrd(self):
		del self._DaysAcrd
		self._DaysAcrd = None

	@property
	def AggtQty(self):
		return self._AggtQty

	@AggtQty.setter
	def AggtQty(self, value):
		self._AggtQty = value if type(value) != auto else self.make_default("AggtQty")

	@AggtQty.deleter
	def AggtQty(self):
		del self._AggtQty
		self._AggtQty = None

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
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if type(value) != auto else self.make_default("AcrdIntrstAmt")

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = None

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if type(value) != auto else self.make_default("BookVal")

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = None

	@property
	def HldgVal(self):
		return self._HldgVal

	@HldgVal.setter
	def HldgVal(self, value):
		self._HldgVal = value if type(value) != auto else self.make_default("HldgVal")

	@HldgVal.deleter
	def HldgVal(self):
		del self._HldgVal
		self._HldgVal = None

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
	def AddtlBalBrkdwnDtls(self):
		return self._AddtlBalBrkdwnDtls

	@AddtlBalBrkdwnDtls.setter
	def AddtlBalBrkdwnDtls(self, value):
		self._AddtlBalBrkdwnDtls = value if type(value) != auto else self.make_default("AddtlBalBrkdwnDtls")

	@AddtlBalBrkdwnDtls.deleter
	def AddtlBalBrkdwnDtls(self):
		del self._AddtlBalBrkdwnDtls
		self._AddtlBalBrkdwnDtls = None

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if type(value) != auto else self.make_default("SfkpgPlc")

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = None

	@property
	def AcrdIntrstAmtSgn(self):
		return self._AcrdIntrstAmtSgn

	@AcrdIntrstAmtSgn.setter
	def AcrdIntrstAmtSgn(self, value):
		self._AcrdIntrstAmtSgn = value if type(value) != auto else self.make_default("AcrdIntrstAmtSgn")

	@AcrdIntrstAmtSgn.deleter
	def AcrdIntrstAmtSgn(self):
		del self._AcrdIntrstAmtSgn
		self._AcrdIntrstAmtSgn = None

	@property
	def BalAtSfkpgPlc(self):
		return self._BalAtSfkpgPlc

	@BalAtSfkpgPlc.setter
	def BalAtSfkpgPlc(self, value):
		self._BalAtSfkpgPlc = value if type(value) != auto else self.make_default("BalAtSfkpgPlc")

	@BalAtSfkpgPlc.deleter
	def BalAtSfkpgPlc(self):
		del self._BalAtSfkpgPlc
		self._BalAtSfkpgPlc = None

	@property
	def PrvsHldgVal(self):
		return self._PrvsHldgVal

	@PrvsHldgVal.setter
	def PrvsHldgVal(self, value):
		self._PrvsHldgVal = value if type(value) != auto else self.make_default("PrvsHldgVal")

	@PrvsHldgVal.deleter
	def PrvsHldgVal(self):
		del self._PrvsHldgVal
		self._PrvsHldgVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalBrkdwnDtls', type=SubBalanceInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtQty', type=BalanceQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcrdIntrstAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BookVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgVal', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwnDtls', type=AdditionalBalanceInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmtSgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAtSfkpgPlc', type=AggregateBalancePerSafekeepingPlace4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsHldgVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

