from . import base_types
from ._Percentage14Rate import Percentage14Rate
from ._RestrictedFINActiveCurrencyAnd13DecimalAmount import RestrictedFINActiveCurrencyAnd13DecimalAmount
from ._AmountAndQuantityRatio5 import AmountAndQuantityRatio5

class SolicitationFeeRateFormat13Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtToQty", "_Rate", "_Amt"]
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
		base_types.FieldEntry(name='AmtToQty', type=AmountAndQuantityRatio5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=Percentage14Rate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Amt', type=RestrictedFINActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=1, array=False),
	))

