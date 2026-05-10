from . import base_types
from .AmountPriceType2Code import AmountPriceType2Code
from .RestrictedFINActiveCurrencyAnd13DecimalAmount import RestrictedFINActiveCurrencyAnd13DecimalAmount

class AmountPrice4(base_types._BaseFieldType):

	__slots__ = ["_AmtPricTp", "_PricVal"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPricTp', type=AmountPriceType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))

