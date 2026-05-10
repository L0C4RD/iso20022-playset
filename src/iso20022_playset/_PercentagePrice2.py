from . import base_types
from ._PriceRateType3Code import PriceRateType3Code
from ._Percentage14Rate import Percentage14Rate

class PercentagePrice2(base_types._BaseFieldType):

	__slots__ = ["_PricVal", "_PctgPricTp"]
	@property
	def PctgPricTp(self):
		return self._PctgPricTp

	@PctgPricTp.setter
	def PctgPricTp(self, value):
		self._PctgPricTp = value if type(value) != base_types.auto else self.make_default("PctgPricTp")

	@PctgPricTp.deleter
	def PctgPricTp(self):
		del self._PctgPricTp
		self._PctgPricTp = None

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
		base_types.FieldEntry(name='PctgPricTp', type=PriceRateType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=Percentage14Rate, min=1, max=1, mutex_group=None, array=False),
	))

