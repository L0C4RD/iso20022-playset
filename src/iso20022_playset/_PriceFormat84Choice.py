# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountPrice5
from . import AmountPricePerAmount3
from . import AmountPricePerFinancialInstrumentQuantity11
from . import PercentagePrice2
from . import PriceValueType9Code
from . import RestrictedFINDecimalNumber

class PriceFormat84Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtPric", "_AmtPricPerAmt", "_AmtPricPerFinInstrmQty", "_IndxPts", "_NotSpcfdPric", "_PctgPric"]
	@property
	def AmtPric(self):
		return self._AmtPric

	@AmtPric.setter
	def AmtPric(self, value):
		self._AmtPric = value if value is not None else base_types.UninitialisedField(self, 'AmtPric', AmountPrice5, False)

	@AmtPric.deleter
	def AmtPric(self):
		del self._AmtPric
		self._AmtPric = base_types.UninitialisedField(self, 'AmtPric', AmountPrice5, False)

	@property
	def AmtPricPerAmt(self):
		return self._AmtPricPerAmt

	@AmtPricPerAmt.setter
	def AmtPricPerAmt(self, value):
		self._AmtPricPerAmt = value if value is not None else base_types.UninitialisedField(self, 'AmtPricPerAmt', AmountPricePerAmount3, False)

	@AmtPricPerAmt.deleter
	def AmtPricPerAmt(self):
		del self._AmtPricPerAmt
		self._AmtPricPerAmt = base_types.UninitialisedField(self, 'AmtPricPerAmt', AmountPricePerAmount3, False)

	@property
	def AmtPricPerFinInstrmQty(self):
		return self._AmtPricPerFinInstrmQty

	@AmtPricPerFinInstrmQty.setter
	def AmtPricPerFinInstrmQty(self, value):
		self._AmtPricPerFinInstrmQty = value if value is not None else base_types.UninitialisedField(self, 'AmtPricPerFinInstrmQty', AmountPricePerFinancialInstrumentQuantity11, False)

	@AmtPricPerFinInstrmQty.deleter
	def AmtPricPerFinInstrmQty(self):
		del self._AmtPricPerFinInstrmQty
		self._AmtPricPerFinInstrmQty = base_types.UninitialisedField(self, 'AmtPricPerFinInstrmQty', AmountPricePerFinancialInstrumentQuantity11, False)

	@property
	def IndxPts(self):
		return self._IndxPts

	@IndxPts.setter
	def IndxPts(self, value):
		self._IndxPts = value if value is not None else base_types.UninitialisedField(self, 'IndxPts', RestrictedFINDecimalNumber, False)

	@IndxPts.deleter
	def IndxPts(self):
		del self._IndxPts
		self._IndxPts = base_types.UninitialisedField(self, 'IndxPts', RestrictedFINDecimalNumber, False)

	@property
	def NotSpcfdPric(self):
		return self._NotSpcfdPric

	@NotSpcfdPric.setter
	def NotSpcfdPric(self, value):
		self._NotSpcfdPric = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfdPric', PriceValueType9Code, False)

	@NotSpcfdPric.deleter
	def NotSpcfdPric(self):
		del self._NotSpcfdPric
		self._NotSpcfdPric = base_types.UninitialisedField(self, 'NotSpcfdPric', PriceValueType9Code, False)

	@property
	def PctgPric(self):
		return self._PctgPric

	@PctgPric.setter
	def PctgPric(self, value):
		self._PctgPric = value if value is not None else base_types.UninitialisedField(self, 'PctgPric', PercentagePrice2, False)

	@PctgPric.deleter
	def PctgPric(self):
		del self._PctgPric
		self._PctgPric = base_types.UninitialisedField(self, 'PctgPric', PercentagePrice2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPric', type=AmountPrice5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerAmt', type=AmountPricePerAmount3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerFinInstrmQty', type=AmountPricePerFinancialInstrumentQuantity11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdPric', type=PriceValueType9Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice2, min=0, max=1, mutex_group=1, array=False),
	))