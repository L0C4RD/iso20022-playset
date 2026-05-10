from . import base_types
from ._RestrictedFINActiveCurrencyAnd13DecimalAmount import RestrictedFINActiveCurrencyAnd13DecimalAmount
from ._AmountPriceType1Code import AmountPriceType1Code

class AmountPricePerAmount3(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_PricVal", "_AmtPricTp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def PricVal(self):
		return self._PricVal

	@PricVal.setter
	def PricVal(self, value):
		self._PricVal = value if type(value) != base_types.auto else self.make_default("PricVal")

	@PricVal.deleter
	def PricVal(self):
		del self._PricVal
		self._PricVal = None

	@property
	def AmtPricTp(self):
		return self._AmtPricTp

	@AmtPricTp.setter
	def AmtPricTp(self, value):
		self._AmtPricTp = value if type(value) != base_types.auto else self.make_default("AmtPricTp")

	@AmtPricTp.deleter
	def AmtPricTp(self):
		del self._AmtPricTp
		self._AmtPricTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtPricTp', type=AmountPriceType1Code, min=1, max=1, mutex_group=None, array=False),
	))

