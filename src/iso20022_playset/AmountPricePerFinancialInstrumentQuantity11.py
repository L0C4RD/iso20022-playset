from . import base_types
import RestrictedFINActiveCurrencyAnd13DecimalAmount
import AmountPriceType1Code
import FinancialInstrumentQuantity36Choice

class AmountPricePerFinancialInstrumentQuantity11(base_types._BaseFieldType):

	__slots__ = ["_AmtPricTp", "_FinInstrmQty", "_PricVal"]
	@property
	def AmtPricTp(self):
		return self._AmtPricTp

	@AmtPricTp.setter
	def AmtPricTp(self, value):
		self._AmtPricTp = value if type(value) != auto else self.make_default("AmtPricTp")

	@AmtPricTp.deleter
	def AmtPricTp(self):
		del self._AmtPricTp
		self._AmtPricTp = None

	@property
	def FinInstrmQty(self):
		return self._FinInstrmQty

	@FinInstrmQty.setter
	def FinInstrmQty(self, value):
		self._FinInstrmQty = value if type(value) != auto else self.make_default("FinInstrmQty")

	@FinInstrmQty.deleter
	def FinInstrmQty(self):
		del self._FinInstrmQty
		self._FinInstrmQty = None

	@property
	def PricVal(self):
		return self._PricVal

	@PricVal.setter
	def PricVal(self, value):
		self._PricVal = value if type(value) != auto else self.make_default("PricVal")

	@PricVal.deleter
	def PricVal(self):
		del self._PricVal
		self._PricVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPricTp', type=AmountPriceType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmQty', type=FinancialInstrumentQuantity36Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))

