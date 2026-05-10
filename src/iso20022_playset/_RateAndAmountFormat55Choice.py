from . import base_types
from ._RateTypeAndPercentageRate12 import RateTypeAndPercentageRate12
from ._Percentage14Rate import Percentage14Rate
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount

class RateAndAmountFormat55Choice(base_types._BaseFieldType):

	__slots__ = ["_RateTpAndRate", "_Rate", "_Amt"]
	@property
	def RateTpAndRate(self):
		return self._RateTpAndRate

	@RateTpAndRate.setter
	def RateTpAndRate(self, value):
		self._RateTpAndRate = value if type(value) != base_types.auto else self.make_default("RateTpAndRate")

	@RateTpAndRate.deleter
	def RateTpAndRate(self):
		del self._RateTpAndRate
		self._RateTpAndRate = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateTpAndRate', type=RateTypeAndPercentageRate12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
	))

