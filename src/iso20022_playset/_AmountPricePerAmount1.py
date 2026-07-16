# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAnd13DecimalAmount
from . import AmountPriceType1FormatChoice

class AmountPricePerAmount1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtPricTp", "_PricVal"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAnd13DecimalAmount, False)

	@property
	def AmtPricTp(self):
		return self._AmtPricTp

	@AmtPricTp.setter
	def AmtPricTp(self, value):
		self._AmtPricTp = value if value is not None else base_types.UninitialisedField(self, 'AmtPricTp', AmountPriceType1FormatChoice, False)

	@AmtPricTp.deleter
	def AmtPricTp(self):
		del self._AmtPricTp
		self._AmtPricTp = base_types.UninitialisedField(self, 'AmtPricTp', AmountPriceType1FormatChoice, False)

	@property
	def PricVal(self):
		return self._PricVal

	@PricVal.setter
	def PricVal(self, value):
		self._PricVal = value if value is not None else base_types.UninitialisedField(self, 'PricVal', ActiveCurrencyAnd13DecimalAmount, False)

	@PricVal.deleter
	def PricVal(self):
		del self._PricVal
		self._PricVal = base_types.UninitialisedField(self, 'PricVal', ActiveCurrencyAnd13DecimalAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtPricTp', type=AmountPriceType1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=ActiveCurrencyAnd13DecimalAmount, min=1, max=1, mutex_group=None, array=False),
	))