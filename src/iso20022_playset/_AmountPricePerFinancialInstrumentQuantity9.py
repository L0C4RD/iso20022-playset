from . import base_types
from ._FinancialInstrumentQuantity1Choice import FinancialInstrumentQuantity1Choice
from ._ISODate import ISODate
from ._PriceRateOrAmount3Choice import PriceRateOrAmount3Choice
from ._YieldedOrValueType1Choice import YieldedOrValueType1Choice

class AmountPricePerFinancialInstrumentQuantity9(base_types._BaseFieldType):

	__slots__ = ["_AmtPricTp", "_FinInstrmQty", "_PricFxgDt", "_PricVal"]
	@property
	def AmtPricTp(self):
		return self._AmtPricTp

	@AmtPricTp.setter
	def AmtPricTp(self, value):
		self._AmtPricTp = value if type(value) != base_types.auto else self.make_default("AmtPricTp")

	@AmtPricTp.deleter
	def AmtPricTp(self):
		del self._AmtPricTp
		self._AmtPricTp = None

	@property
	def FinInstrmQty(self):
		return self._FinInstrmQty

	@FinInstrmQty.setter
	def FinInstrmQty(self, value):
		self._FinInstrmQty = value if type(value) != base_types.auto else self.make_default("FinInstrmQty")

	@FinInstrmQty.deleter
	def FinInstrmQty(self):
		del self._FinInstrmQty
		self._FinInstrmQty = None

	@property
	def PricFxgDt(self):
		return self._PricFxgDt

	@PricFxgDt.setter
	def PricFxgDt(self, value):
		self._PricFxgDt = value if type(value) != base_types.auto else self.make_default("PricFxgDt")

	@PricFxgDt.deleter
	def PricFxgDt(self):
		del self._PricFxgDt
		self._PricFxgDt = None

	@property
	def PricVal(self):
		return self._PricVal

	@PricVal.setter
	def PricVal(self, value):
		self._PricVal = value if type(value) != base_types.auto else self.make_default("PricVal")

	@PricVal.deleter
	def PricVal(self):
		del self._PricVal
		self._PricVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPricTp', type=YieldedOrValueType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricFxgDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=PriceRateOrAmount3Choice, min=1, max=1, mutex_group=None, array=False),
	))

