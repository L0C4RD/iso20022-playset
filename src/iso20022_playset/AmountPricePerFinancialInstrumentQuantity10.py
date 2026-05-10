import base_types
import ActiveCurrencyAnd13DecimalAmount
import AmountPriceType1Code
import FinancialInstrumentQuantity33Choice

class AmountPricePerFinancialInstrumentQuantity10(base_types._BaseFieldType):

	__slots__ = ["_PricVal", "_FinInstrmQty", "_AmtPricTp"]
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
	def AmtPricTp(self):
		return self._AmtPricTp

	@AmtPricTp.setter
	def AmtPricTp(self, value):
		self._AmtPricTp = value if type(value) != auto else self.make_default("AmtPricTp")

	@AmtPricTp.deleter
	def AmtPricTp(self):
		del self._AmtPricTp
		self._AmtPricTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricVal', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmQty', type=FinancialInstrumentQuantity33Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtPricTp', type=AmountPriceType1Code, min=1, max=1, mutex_group=None, array=False),
	))

