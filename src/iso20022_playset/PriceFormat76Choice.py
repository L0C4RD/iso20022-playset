from . import base_types
import PercentagePrice2
import AmountPricePerAmount2
import DecimalNumber
import AmountPricePerFinancialInstrumentQuantity10
import AmountPrice3

class PriceFormat76Choice(base_types._BaseFieldType):

	__slots__ = ["_PctgPric", "_IndxPts", "_AmtPric", "_AmtPricPerFinInstrmQty", "_AmtPricPerAmt"]
	@property
	def PctgPric(self):
		return self._PctgPric

	@PctgPric.setter
	def PctgPric(self, value):
		self._PctgPric = value if type(value) != auto else self.make_default("PctgPric")

	@PctgPric.deleter
	def PctgPric(self):
		del self._PctgPric
		self._PctgPric = None

	@property
	def IndxPts(self):
		return self._IndxPts

	@IndxPts.setter
	def IndxPts(self, value):
		self._IndxPts = value if type(value) != auto else self.make_default("IndxPts")

	@IndxPts.deleter
	def IndxPts(self):
		del self._IndxPts
		self._IndxPts = None

	@property
	def AmtPric(self):
		return self._AmtPric

	@AmtPric.setter
	def AmtPric(self, value):
		self._AmtPric = value if type(value) != auto else self.make_default("AmtPric")

	@AmtPric.deleter
	def AmtPric(self):
		del self._AmtPric
		self._AmtPric = None

	@property
	def AmtPricPerFinInstrmQty(self):
		return self._AmtPricPerFinInstrmQty

	@AmtPricPerFinInstrmQty.setter
	def AmtPricPerFinInstrmQty(self, value):
		self._AmtPricPerFinInstrmQty = value if type(value) != auto else self.make_default("AmtPricPerFinInstrmQty")

	@AmtPricPerFinInstrmQty.deleter
	def AmtPricPerFinInstrmQty(self):
		del self._AmtPricPerFinInstrmQty
		self._AmtPricPerFinInstrmQty = None

	@property
	def AmtPricPerAmt(self):
		return self._AmtPricPerAmt

	@AmtPricPerAmt.setter
	def AmtPricPerAmt(self, value):
		self._AmtPricPerAmt = value if type(value) != auto else self.make_default("AmtPricPerAmt")

	@AmtPricPerAmt.deleter
	def AmtPricPerAmt(self):
		del self._AmtPricPerAmt
		self._AmtPricPerAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PctgPric', type=PercentagePrice2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndxPts', type=DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPric', type=AmountPrice3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerFinInstrmQty', type=AmountPricePerFinancialInstrumentQuantity10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerAmt', type=AmountPricePerAmount2, min=0, max=1, mutex_group=1, array=False),
	))

