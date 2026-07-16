# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndQuantityRatio1
from . import AmountToAmountRatio1
from . import QuantityToQuantityRatio1
from . import RateType12FormatChoice

class RatioFormat2Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtToAmt", "_AmtToQty", "_NotSpcfdRate", "_QtyToAmt", "_QtyToQty"]
	@property
	def AmtToAmt(self):
		return self._AmtToAmt

	@AmtToAmt.setter
	def AmtToAmt(self, value):
		self._AmtToAmt = value if value is not None else base_types.UninitialisedField(self, 'AmtToAmt', AmountToAmountRatio1, False)

	@AmtToAmt.deleter
	def AmtToAmt(self):
		del self._AmtToAmt
		self._AmtToAmt = base_types.UninitialisedField(self, 'AmtToAmt', AmountToAmountRatio1, False)

	@property
	def AmtToQty(self):
		return self._AmtToQty

	@AmtToQty.setter
	def AmtToQty(self, value):
		self._AmtToQty = value if value is not None else base_types.UninitialisedField(self, 'AmtToQty', AmountAndQuantityRatio1, False)

	@AmtToQty.deleter
	def AmtToQty(self):
		del self._AmtToQty
		self._AmtToQty = base_types.UninitialisedField(self, 'AmtToQty', AmountAndQuantityRatio1, False)

	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdRate', RateType12FormatChoice, False)

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = base_types.UninitialisedField(self, 'NotSpcfdRate', RateType12FormatChoice, False)

	@property
	def QtyToAmt(self):
		return self._QtyToAmt

	@QtyToAmt.setter
	def QtyToAmt(self, value):
		self._QtyToAmt = value if value is not None else base_types.UninitialisedField(self, 'QtyToAmt', AmountAndQuantityRatio1, False)

	@QtyToAmt.deleter
	def QtyToAmt(self):
		del self._QtyToAmt
		self._QtyToAmt = base_types.UninitialisedField(self, 'QtyToAmt', AmountAndQuantityRatio1, False)

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
		base_types.FieldEntry(name='AmtToAmt', type=AmountToAmountRatio1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtToQty', type=AmountAndQuantityRatio1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateType12FormatChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToAmt', type=AmountAndQuantityRatio1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='QtyToQty', type=QuantityToQuantityRatio1, min=0, max=1, mutex_group=1, array=False),
	))