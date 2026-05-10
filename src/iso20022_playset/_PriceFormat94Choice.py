from . import base_types
from ._AmountPricePerAmount3 import AmountPricePerAmount3
from ._RestrictedFINDecimalNumber import RestrictedFINDecimalNumber
from ._PriceValueType8Code import PriceValueType8Code
from ._AmountPricePerFinancialInstrumentQuantity11 import AmountPricePerFinancialInstrumentQuantity11
from ._PercentagePrice3 import PercentagePrice3
from ._AmountPrice5 import AmountPrice5

class PriceFormat94Choice(base_types._BaseFieldType):

	__slots__ = ["_AmtPricPerFinInstrmQty", "_PctgPric", "_NotSpcfdPric", "_AmtPric", "_AmtPricPerAmt", "_IndxPts"]
	@property
	def AmtPric(self):
		return self._AmtPric

	@AmtPric.setter
	def AmtPric(self, value):
		self._AmtPric = value if type(value) != base_types.auto else self.make_default("AmtPric")

	@AmtPric.deleter
	def AmtPric(self):
		del self._AmtPric
		self._AmtPric = None

	@property
	def AmtPricPerAmt(self):
		return self._AmtPricPerAmt

	@AmtPricPerAmt.setter
	def AmtPricPerAmt(self, value):
		self._AmtPricPerAmt = value if type(value) != base_types.auto else self.make_default("AmtPricPerAmt")

	@AmtPricPerAmt.deleter
	def AmtPricPerAmt(self):
		del self._AmtPricPerAmt
		self._AmtPricPerAmt = None

	@property
	def AmtPricPerFinInstrmQty(self):
		return self._AmtPricPerFinInstrmQty

	@AmtPricPerFinInstrmQty.setter
	def AmtPricPerFinInstrmQty(self, value):
		self._AmtPricPerFinInstrmQty = value if type(value) != base_types.auto else self.make_default("AmtPricPerFinInstrmQty")

	@AmtPricPerFinInstrmQty.deleter
	def AmtPricPerFinInstrmQty(self):
		del self._AmtPricPerFinInstrmQty
		self._AmtPricPerFinInstrmQty = None

	@property
	def IndxPts(self):
		return self._IndxPts

	@IndxPts.setter
	def IndxPts(self, value):
		self._IndxPts = value if type(value) != base_types.auto else self.make_default("IndxPts")

	@IndxPts.deleter
	def IndxPts(self):
		del self._IndxPts
		self._IndxPts = None

	@property
	def NotSpcfdPric(self):
		return self._NotSpcfdPric

	@NotSpcfdPric.setter
	def NotSpcfdPric(self, value):
		self._NotSpcfdPric = value if type(value) != base_types.auto else self.make_default("NotSpcfdPric")

	@NotSpcfdPric.deleter
	def NotSpcfdPric(self):
		del self._NotSpcfdPric
		self._NotSpcfdPric = None

	@property
	def PctgPric(self):
		return self._PctgPric

	@PctgPric.setter
	def PctgPric(self, value):
		self._PctgPric = value if type(value) != base_types.auto else self.make_default("PctgPric")

	@PctgPric.deleter
	def PctgPric(self):
		del self._PctgPric
		self._PctgPric = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPric', type=AmountPrice5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerAmt', type=AmountPricePerAmount3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerFinInstrmQty', type=AmountPricePerFinancialInstrumentQuantity11, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=RestrictedFINDecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdPric', type=PriceValueType8Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice3, min=0, max=1, mutex_group=1, array=False),
	))

