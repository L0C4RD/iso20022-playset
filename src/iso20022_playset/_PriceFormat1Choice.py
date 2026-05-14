# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmountPrice1 import AmountPrice1
from ._AmountPricePerAmount1 import AmountPricePerAmount1
from ._AmountPricePerFinancialInstrumentQuantity1 import AmountPricePerFinancialInstrumentQuantity1
from ._PercentageRate import PercentageRate
from ._PriceValueType6FormatChoice import PriceValueType6FormatChoice

class PriceFormat1Choice(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_AmtPricPerAmt", "_AmtPricPerFinInstrmQty", "_NotSpcfd", "_Rate"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

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
	def NotSpcfd(self):
		return self._NotSpcfd

	@NotSpcfd.setter
	def NotSpcfd(self, value):
		self._NotSpcfd = value if type(value) != base_types.auto else self.make_default("NotSpcfd")

	@NotSpcfd.deleter
	def NotSpcfd(self):
		del self._NotSpcfd
		self._NotSpcfd = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=AmountPrice1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerAmt', type=AmountPricePerAmount1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AmtPricPerFinInstrmQty', type=AmountPricePerFinancialInstrumentQuantity1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfd', type=PriceValueType6FormatChoice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))