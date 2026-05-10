import base_types
import QuantityToQuantityRatio2
import AmountAndQuantityRatio5
import AmountToAmountRatio3
import RateValueType7Code

class RatioFormat24Choice(base_types._BaseFieldType):

	__slots__ = ["_QtyToAmt", "_NotSpcfdRate", "_QtyToQty", "_AmtToQty", "_AmtToAmt"]
	@property
	def QtyToAmt(self):
		return self._QtyToAmt

	@QtyToAmt.setter
	def QtyToAmt(self, value):
		self._QtyToAmt = value if type(value) != auto else self.make_default("QtyToAmt")

	@QtyToAmt.deleter
	def QtyToAmt(self):
		del self._QtyToAmt
		self._QtyToAmt = None

	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if type(value) != auto else self.make_default("NotSpcfdRate")

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = None

	@property
	def QtyToQty(self):
		return self._QtyToQty

	@QtyToQty.setter
	def QtyToQty(self, value):
		self._QtyToQty = value if type(value) != auto else self.make_default("QtyToQty")

	@QtyToQty.deleter
	def QtyToQty(self):
		del self._QtyToQty
		self._QtyToQty = None

	@property
	def AmtToQty(self):
		return self._AmtToQty

	@AmtToQty.setter
	def AmtToQty(self, value):
		self._AmtToQty = value if type(value) != auto else self.make_default("AmtToQty")

	@AmtToQty.deleter
	def AmtToQty(self):
		del self._AmtToQty
		self._AmtToQty = None

	@property
	def AmtToAmt(self):
		return self._AmtToAmt

	@AmtToAmt.setter
	def AmtToAmt(self, value):
		self._AmtToAmt = value if type(value) != auto else self.make_default("AmtToAmt")

	@AmtToAmt.deleter
	def AmtToAmt(self):
		del self._AmtToAmt
		self._AmtToAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtyToAmt', type=AmountAndQuantityRatio5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType7Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToQty', type=AmountAndQuantityRatio5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio3, min=0, max=1, mutex_group=1, array=False),
	))

