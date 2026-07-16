# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountToAmountRatio2
from . import QuantityToQuantityRatio1
from . import RateValueType7Code

class RatioFormat17Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtToAmt", "_NotSpcfdRate", "_QtyToQty"]
	@property
	def AmtToAmt(self):
		return self._AmtToAmt

	@AmtToAmt.setter
	def AmtToAmt(self, value):
		self._AmtToAmt = value if value is not None else base_types.UninitialisedField(self, 'AmtToAmt', AmountToAmountRatio2, False)

	@AmtToAmt.deleter
	def AmtToAmt(self):
		del self._AmtToAmt
		self._AmtToAmt = base_types.UninitialisedField(self, 'AmtToAmt', AmountToAmountRatio2, False)

	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdRate', RateValueType7Code, False)

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = base_types.UninitialisedField(self, 'NotSpcfdRate', RateValueType7Code, False)

	@property
	def QtyToQty(self):
		return self._QtyToQty

	@QtyToQty.setter
	def QtyToQty(self, value):
		self._QtyToQty = value if value is not None else base_types.UninitialisedField(self, 'QtyToQty', QuantityToQuantityRatio1, False)

	@QtyToQty.deleter
	def QtyToQty(self):
		del self._QtyToQty
		self._QtyToQty = base_types.UninitialisedField(self, 'QtyToQty', QuantityToQuantityRatio1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateValueType7Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=1, array=False),
	))