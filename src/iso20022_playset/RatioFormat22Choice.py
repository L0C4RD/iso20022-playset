from . import base_types
import AmountAndQuantityRatio5
import QuantityToQuantityRatio2
import AmountToAmountRatio3

class RatioFormat22Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtToQty", "_QtyToAmt", "_AmtToAmt", "_QtyToQty"]
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
	def AmtToAmt(self):
		return self._AmtToAmt

	@AmtToAmt.setter
	def AmtToAmt(self, value):
		self._AmtToAmt = value if type(value) != auto else self.make_default("AmtToAmt")

	@AmtToAmt.deleter
	def AmtToAmt(self):
		del self._AmtToAmt
		self._AmtToAmt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToQty', type=AmountAndQuantityRatio5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToAmt', type=AmountAndQuantityRatio5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio2, min=0, max=1, mutex_group=1, array=False),
	))

