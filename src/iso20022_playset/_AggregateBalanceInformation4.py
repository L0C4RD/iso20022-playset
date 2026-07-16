# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import AdditionalBalanceInformation2
from . import AggregateBalancePerSafekeepingPlace3
from . import BalanceQuantity1Choice
from . import FinancialInstrument13
from . import ForeignExchangeTerms6
from . import Number
from . import PlusOrMinusIndicator
from . import PriceInformation2
from . import SafekeepingPlaceFormatChoice
from . import SubBalanceInformation2

class AggregateBalanceInformation4(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrstAmt", "_AcrdIntrstAmtSgn", "_AddtlBalBrkdwnDtls", "_AggtQty", "_AvlblQty", "_BalAtSfkpgPlc", "_BalBrkdwnDtls", "_BookVal", "_DaysAcrd", "_FXDtls", "_FinInstrmDtls", "_HldgVal", "_NotAvlblQty", "_PricDtls", "_PrvsHldgVal", "_SfkpgPlc"]
	@property
	def AcrdIntrstAmt(self):
		return self._AcrdIntrstAmt

	@AcrdIntrstAmt.setter
	def AcrdIntrstAmt(self, value):
		self._AcrdIntrstAmt = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@AcrdIntrstAmt.deleter
	def AcrdIntrstAmt(self):
		del self._AcrdIntrstAmt
		self._AcrdIntrstAmt = base_types.UninitialisedField(self, 'AcrdIntrstAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def AcrdIntrstAmtSgn(self):
		return self._AcrdIntrstAmtSgn

	@AcrdIntrstAmtSgn.setter
	def AcrdIntrstAmtSgn(self, value):
		self._AcrdIntrstAmtSgn = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrstAmtSgn', PlusOrMinusIndicator, False)

	@AcrdIntrstAmtSgn.deleter
	def AcrdIntrstAmtSgn(self):
		del self._AcrdIntrstAmtSgn
		self._AcrdIntrstAmtSgn = base_types.UninitialisedField(self, 'AcrdIntrstAmtSgn', PlusOrMinusIndicator, False)

	@property
	def AddtlBalBrkdwnDtls(self):
		return self._AddtlBalBrkdwnDtls

	@AddtlBalBrkdwnDtls.setter
	def AddtlBalBrkdwnDtls(self, value):
		self._AddtlBalBrkdwnDtls = value if value is not None else base_types.UninitialisedField(self, 'AddtlBalBrkdwnDtls', AdditionalBalanceInformation2, True)

	@AddtlBalBrkdwnDtls.deleter
	def AddtlBalBrkdwnDtls(self):
		del self._AddtlBalBrkdwnDtls
		self._AddtlBalBrkdwnDtls = base_types.UninitialisedField(self, 'AddtlBalBrkdwnDtls', AdditionalBalanceInformation2, True)

	@property
	def AggtQty(self):
		return self._AggtQty

	@AggtQty.setter
	def AggtQty(self, value):
		self._AggtQty = value if value is not None else base_types.UninitialisedField(self, 'AggtQty', BalanceQuantity1Choice, False)

	@AggtQty.deleter
	def AggtQty(self):
		del self._AggtQty
		self._AggtQty = base_types.UninitialisedField(self, 'AggtQty', BalanceQuantity1Choice, False)

	@property
	def AvlblQty(self):
		return self._AvlblQty

	@AvlblQty.setter
	def AvlblQty(self, value):
		self._AvlblQty = value if value is not None else base_types.UninitialisedField(self, 'AvlblQty', BalanceQuantity1Choice, False)

	@AvlblQty.deleter
	def AvlblQty(self):
		del self._AvlblQty
		self._AvlblQty = base_types.UninitialisedField(self, 'AvlblQty', BalanceQuantity1Choice, False)

	@property
	def BalAtSfkpgPlc(self):
		return self._BalAtSfkpgPlc

	@BalAtSfkpgPlc.setter
	def BalAtSfkpgPlc(self, value):
		self._BalAtSfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'BalAtSfkpgPlc', AggregateBalancePerSafekeepingPlace3, True)

	@BalAtSfkpgPlc.deleter
	def BalAtSfkpgPlc(self):
		del self._BalAtSfkpgPlc
		self._BalAtSfkpgPlc = base_types.UninitialisedField(self, 'BalAtSfkpgPlc', AggregateBalancePerSafekeepingPlace3, True)

	@property
	def BalBrkdwnDtls(self):
		return self._BalBrkdwnDtls

	@BalBrkdwnDtls.setter
	def BalBrkdwnDtls(self, value):
		self._BalBrkdwnDtls = value if value is not None else base_types.UninitialisedField(self, 'BalBrkdwnDtls', SubBalanceInformation2, True)

	@BalBrkdwnDtls.deleter
	def BalBrkdwnDtls(self):
		del self._BalBrkdwnDtls
		self._BalBrkdwnDtls = base_types.UninitialisedField(self, 'BalBrkdwnDtls', SubBalanceInformation2, True)

	@property
	def BookVal(self):
		return self._BookVal

	@BookVal.setter
	def BookVal(self, value):
		self._BookVal = value if value is not None else base_types.UninitialisedField(self, 'BookVal', ActiveOrHistoricCurrencyAndAmount, False)

	@BookVal.deleter
	def BookVal(self):
		del self._BookVal
		self._BookVal = base_types.UninitialisedField(self, 'BookVal', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def DaysAcrd(self):
		return self._DaysAcrd

	@DaysAcrd.setter
	def DaysAcrd(self, value):
		self._DaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'DaysAcrd', Number, False)

	@DaysAcrd.deleter
	def DaysAcrd(self):
		del self._DaysAcrd
		self._DaysAcrd = base_types.UninitialisedField(self, 'DaysAcrd', Number, False)

	@property
	def FXDtls(self):
		return self._FXDtls

	@FXDtls.setter
	def FXDtls(self, value):
		self._FXDtls = value if value is not None else base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms6, False)

	@FXDtls.deleter
	def FXDtls(self):
		del self._FXDtls
		self._FXDtls = base_types.UninitialisedField(self, 'FXDtls', ForeignExchangeTerms6, False)

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument13, False)

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = base_types.UninitialisedField(self, 'FinInstrmDtls', FinancialInstrument13, False)

	@property
	def HldgVal(self):
		return self._HldgVal

	@HldgVal.setter
	def HldgVal(self, value):
		self._HldgVal = value if value is not None else base_types.UninitialisedField(self, 'HldgVal', ActiveOrHistoricCurrencyAndAmount, True)

	@HldgVal.deleter
	def HldgVal(self):
		del self._HldgVal
		self._HldgVal = base_types.UninitialisedField(self, 'HldgVal', ActiveOrHistoricCurrencyAndAmount, True)

	@property
	def NotAvlblQty(self):
		return self._NotAvlblQty

	@NotAvlblQty.setter
	def NotAvlblQty(self, value):
		self._NotAvlblQty = value if value is not None else base_types.UninitialisedField(self, 'NotAvlblQty', BalanceQuantity1Choice, False)

	@NotAvlblQty.deleter
	def NotAvlblQty(self):
		del self._NotAvlblQty
		self._NotAvlblQty = base_types.UninitialisedField(self, 'NotAvlblQty', BalanceQuantity1Choice, False)

	@property
	def PricDtls(self):
		return self._PricDtls

	@PricDtls.setter
	def PricDtls(self, value):
		self._PricDtls = value if value is not None else base_types.UninitialisedField(self, 'PricDtls', PriceInformation2, True)

	@PricDtls.deleter
	def PricDtls(self):
		del self._PricDtls
		self._PricDtls = base_types.UninitialisedField(self, 'PricDtls', PriceInformation2, True)

	@property
	def PrvsHldgVal(self):
		return self._PrvsHldgVal

	@PrvsHldgVal.setter
	def PrvsHldgVal(self, value):
		self._PrvsHldgVal = value if value is not None else base_types.UninitialisedField(self, 'PrvsHldgVal', ActiveOrHistoricCurrencyAndAmount, False)

	@PrvsHldgVal.deleter
	def PrvsHldgVal(self):
		del self._PrvsHldgVal
		self._PrvsHldgVal = base_types.UninitialisedField(self, 'PrvsHldgVal', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def SfkpgPlc(self):
		return self._SfkpgPlc

	@SfkpgPlc.setter
	def SfkpgPlc(self, value):
		self._SfkpgPlc = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormatChoice, False)

	@SfkpgPlc.deleter
	def SfkpgPlc(self):
		del self._SfkpgPlc
		self._SfkpgPlc = base_types.UninitialisedField(self, 'SfkpgPlc', SafekeepingPlaceFormatChoice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrstAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcrdIntrstAmtSgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlBalBrkdwnDtls', type=AdditionalBalanceInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AggtQty', type=BalanceQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvlblQty', type=BalanceQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalAtSfkpgPlc', type=AggregateBalancePerSafekeepingPlace3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BalBrkdwnDtls', type=SubBalanceInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BookVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DaysAcrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXDtls', type=ForeignExchangeTerms6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HldgVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NotAvlblQty', type=BalanceQuantity1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricDtls', type=PriceInformation2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvsHldgVal', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlc', type=SafekeepingPlaceFormatChoice, min=0, max=1, mutex_group=None, array=False),
	))