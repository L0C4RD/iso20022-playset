from . import base_types
from ._ActiveCurrencyAnd13DecimalAmount import ActiveCurrencyAnd13DecimalAmount
from ._AmountAndQuantityRatio4 import AmountAndQuantityRatio4
from ._Percentage14Rate import Percentage14Rate
from ._RateValueType7Code import RateValueType7Code

class SolicitationFeeRateFormat11Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtToQty", "_NotSpcfdRate", "_Rate"]
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
	def AmtToQty(self):
		return self._AmtToQty

	@AmtToQty.setter
	def AmtToQty(self, value):
		self._AmtToQty = value if type(value) != base_types.auto else self.make_default("AmtToQty")

	@AmtToQty.deleter
	def AmtToQty(self):
		del self._AmtToQty
		self._AmtToQty = None

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
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToQty', type=AmountAndQuantityRatio4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType7Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
	))

