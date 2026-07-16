# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountPrice1
from . import AmountPricePerAmount1
from . import AmountPricePerFinancialInstrumentQuantity1
from . import PercentageRate
from . import PriceValueType6FormatChoice

class PriceFormat1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtPricPerAmt", "_AmtPricPerFinInstrmQty", "_NotSpcfd", "_Rate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountPrice1, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountPrice1, False)

	@property
	def AmtPricPerAmt(self):
		return self._AmtPricPerAmt

	@AmtPricPerAmt.setter
	def AmtPricPerAmt(self, value):
		self._AmtPricPerAmt = value if value is not None else base_types.UninitialisedField(self, 'AmtPricPerAmt', AmountPricePerAmount1, False)

	@AmtPricPerAmt.deleter
	def AmtPricPerAmt(self):
		del self._AmtPricPerAmt
		self._AmtPricPerAmt = base_types.UninitialisedField(self, 'AmtPricPerAmt', AmountPricePerAmount1, False)

	@property
	def AmtPricPerFinInstrmQty(self):
		return self._AmtPricPerFinInstrmQty

	@AmtPricPerFinInstrmQty.setter
	def AmtPricPerFinInstrmQty(self, value):
		self._AmtPricPerFinInstrmQty = value if value is not None else base_types.UninitialisedField(self, 'AmtPricPerFinInstrmQty', AmountPricePerFinancialInstrumentQuantity1, False)

	@AmtPricPerFinInstrmQty.deleter
	def AmtPricPerFinInstrmQty(self):
		del self._AmtPricPerFinInstrmQty
		self._AmtPricPerFinInstrmQty = base_types.UninitialisedField(self, 'AmtPricPerFinInstrmQty', AmountPricePerFinancialInstrumentQuantity1, False)

	@property
	def NotSpcfd(self):
		return self._NotSpcfd

	@NotSpcfd.setter
	def NotSpcfd(self, value):
		self._NotSpcfd = value if value is not None else base_types.UninitialisedField(self, 'NotSpcfd', PriceValueType6FormatChoice, False)

	@NotSpcfd.deleter
	def NotSpcfd(self):
		del self._NotSpcfd
		self._NotSpcfd = base_types.UninitialisedField(self, 'NotSpcfd', PriceValueType6FormatChoice, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountPrice1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerAmt', type=AmountPricePerAmount1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerFinInstrmQty', type=AmountPricePerFinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfd', type=PriceValueType6FormatChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))