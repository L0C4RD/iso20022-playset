from . import base_types
from ._AmountToAmountRatio3 import AmountToAmountRatio3
from ._QuantityToQuantityRatio2 import QuantityToQuantityRatio2
from ._RateValueType7Code import RateValueType7Code

class RatioFormat23Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtToAmt", "_NotSpcfdRate", "_QtyToQty"]
	@property
	def AmtToAmt(self):
		return self._AmtToAmt

	@AmtToAmt.setter
	def AmtToAmt(self, value):
		self._AmtToAmt = value if type(value) != base_types.auto else self.make_default("AmtToAmt")

	@AmtToAmt.deleter
	def AmtToAmt(self):
		del self._AmtToAmt
		self._AmtToAmt = None

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
	def QtyToQty(self):
		return self._QtyToQty

	@QtyToQty.setter
	def QtyToQty(self, value):
		self._QtyToQty = value if type(value) != base_types.auto else self.make_default("QtyToQty")

	@QtyToQty.deleter
	def QtyToQty(self):
		del self._QtyToQty
		self._QtyToQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType7Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio2, min=0, max=1, mutex_group=1, array=False),
	))

