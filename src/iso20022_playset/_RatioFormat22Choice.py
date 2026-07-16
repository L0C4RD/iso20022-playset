# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndQuantityRatio5
from . import AmountToAmountRatio3
from . import QuantityToQuantityRatio2

class RatioFormat22Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtToAmt", "_AmtToQty", "_QtyToAmt", "_QtyToQty"]
	@property
	def AmtToAmt(self):
		return self._AmtToAmt

	@AmtToAmt.setter
	def AmtToAmt(self, value):
		self._AmtToAmt = value if value is not None else base_types.UninitialisedField(self, 'AmtToAmt', AmountToAmountRatio3, False)

	@AmtToAmt.deleter
	def AmtToAmt(self):
		del self._AmtToAmt
		self._AmtToAmt = base_types.UninitialisedField(self, 'AmtToAmt', AmountToAmountRatio3, False)

	@property
	def AmtToQty(self):
		return self._AmtToQty

	@AmtToQty.setter
	def AmtToQty(self, value):
		self._AmtToQty = value if value is not None else base_types.UninitialisedField(self, 'AmtToQty', AmountAndQuantityRatio5, False)

	@AmtToQty.deleter
	def AmtToQty(self):
		del self._AmtToQty
		self._AmtToQty = base_types.UninitialisedField(self, 'AmtToQty', AmountAndQuantityRatio5, False)

	@property
	def QtyToAmt(self):
		return self._QtyToAmt

	@QtyToAmt.setter
	def QtyToAmt(self, value):
		self._QtyToAmt = value if value is not None else base_types.UninitialisedField(self, 'QtyToAmt', AmountAndQuantityRatio5, False)

	@QtyToAmt.deleter
	def QtyToAmt(self):
		del self._QtyToAmt
		self._QtyToAmt = base_types.UninitialisedField(self, 'QtyToAmt', AmountAndQuantityRatio5, False)

	@property
	def QtyToQty(self):
		return self._QtyToQty

	@QtyToQty.setter
	def QtyToQty(self, value):
		self._QtyToQty = value if value is not None else base_types.UninitialisedField(self, 'QtyToQty', QuantityToQuantityRatio2, False)

	@QtyToQty.deleter
	def QtyToQty(self):
		del self._QtyToQty
		self._QtyToQty = base_types.UninitialisedField(self, 'QtyToQty', QuantityToQuantityRatio2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToQty', type=AmountAndQuantityRatio5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToAmt', type=AmountAndQuantityRatio5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio2, min=0, max=1, mutex_group=1, array=False),
	))