# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity1Choice
from . import ISODate
from . import PriceRateOrAmount3Choice
from . import YieldedOrValueType1Choice

class AmountPricePerFinancialInstrumentQuantity9(base_types._BaseFieldType):

	__slots__ = ["_AmtPricTp", "_FinInstrmQty", "_PricFxgDt", "_PricVal"]
	@property
	def AmtPricTp(self):
		return self._AmtPricTp

	@AmtPricTp.setter
	def AmtPricTp(self, value):
		self._AmtPricTp = value if value is not None else base_types.UninitialisedField(self, 'AmtPricTp', YieldedOrValueType1Choice, False)

	@AmtPricTp.deleter
	def AmtPricTp(self):
		del self._AmtPricTp
		self._AmtPricTp = base_types.UninitialisedField(self, 'AmtPricTp', YieldedOrValueType1Choice, False)

	@property
	def FinInstrmQty(self):
		return self._FinInstrmQty

	@FinInstrmQty.setter
	def FinInstrmQty(self, value):
		self._FinInstrmQty = value if value is not None else base_types.UninitialisedField(self, 'FinInstrmQty', FinancialInstrumentQuantity1Choice, False)

	@FinInstrmQty.deleter
	def FinInstrmQty(self):
		del self._FinInstrmQty
		self._FinInstrmQty = base_types.UninitialisedField(self, 'FinInstrmQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def PricFxgDt(self):
		return self._PricFxgDt

	@PricFxgDt.setter
	def PricFxgDt(self, value):
		self._PricFxgDt = value if value is not None else base_types.UninitialisedField(self, 'PricFxgDt', ISODate, False)

	@PricFxgDt.deleter
	def PricFxgDt(self):
		del self._PricFxgDt
		self._PricFxgDt = base_types.UninitialisedField(self, 'PricFxgDt', ISODate, False)

	@property
	def PricVal(self):
		return self._PricVal

	@PricVal.setter
	def PricVal(self, value):
		self._PricVal = value if value is not None else base_types.UninitialisedField(self, 'PricVal', PriceRateOrAmount3Choice, False)

	@PricVal.deleter
	def PricVal(self):
		del self._PricVal
		self._PricVal = base_types.UninitialisedField(self, 'PricVal', PriceRateOrAmount3Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtPricTp', type=YieldedOrValueType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricFxgDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=PriceRateOrAmount3Choice, min=1, max=1, mutex_group=None, array=False),
	))