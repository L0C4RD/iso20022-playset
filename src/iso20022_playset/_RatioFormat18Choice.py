from . import base_types
from ._AmountToAmountRatio2 import AmountToAmountRatio2
from ._RateValueType7Code import RateValueType7Code
from ._AmountAndQuantityRatio4 import AmountAndQuantityRatio4
from ._QuantityToQuantityRatio1 import QuantityToQuantityRatio1

class RatioFormat18Choice(base_types._BaseFieldType):

	__slots__ = ["_QtyToQty", "_AmtToAmt", "_NotSpcfdRate", "_QtyToAmt", "_AmtToQty"]
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
	def QtyToAmt(self):
		return self._QtyToAmt

	@QtyToAmt.setter
	def QtyToAmt(self, value):
		self._QtyToAmt = value if type(value) != base_types.auto else self.make_default("QtyToAmt")

	@QtyToAmt.deleter
	def QtyToAmt(self):
		del self._QtyToAmt
		self._QtyToAmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType7Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToAmt', type=AmountAndQuantityRatio4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToQty', type=AmountAndQuantityRatio4, min=0, max=1, mutex_group=1, array=False),
	))

