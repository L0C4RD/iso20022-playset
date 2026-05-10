from . import base_types
import AmountToAmountRatio2
import QuantityToQuantityRatio1

class RatioFormat20Choice(base_types._BaseFieldType):

	__slots__ = ["_QtyToQty", "_AmtToAmt"]
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
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio2, min=0, max=1, mutex_group=1, array=False),
	))

