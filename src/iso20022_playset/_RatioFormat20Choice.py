# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountToAmountRatio2 import AmountToAmountRatio2
from ._QuantityToQuantityRatio1 import QuantityToQuantityRatio1

class RatioFormat20Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtToAmt", "_QtyToQty"]
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
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=1, array=False),
	))