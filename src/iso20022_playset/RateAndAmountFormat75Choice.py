from . import base_types
from .Percentage14Rate import Percentage14Rate
from .RestrictedFINActiveCurrencyAnd13DecimalAmount import RestrictedFINActiveCurrencyAnd13DecimalAmount
from .RateTypeAndPercentageRate20 import RateTypeAndPercentageRate20
from .RateValueType7Code import RateValueType7Code

class RateAndAmountFormat75Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_RateTpAndRate", "_NotSpcfdRate", "_Rate"]
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
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if type(value) != base_types.auto else self.make_default("NotSpcfdRate")

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateTpAndRate', type=RateTypeAndPercentageRate20, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType7Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
	))

