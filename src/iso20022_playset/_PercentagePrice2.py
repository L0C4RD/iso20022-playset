# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Percentage14Rate
from . import PriceRateType3Code

class PercentagePrice2(base_types._BaseFieldType):

	__slots__ = ["_PctgPricTp", "_PricVal"]
	@property
	def PctgPricTp(self):
		return self._PctgPricTp

	@PctgPricTp.setter
	def PctgPricTp(self, value):
		self._PctgPricTp = value if value is not None else base_types.UninitialisedField(self, 'PctgPricTp', PriceRateType3Code, False)

	@PctgPricTp.deleter
	def PctgPricTp(self):
		del self._PctgPricTp
		self._PctgPricTp = base_types.UninitialisedField(self, 'PctgPricTp', PriceRateType3Code, False)

	@property
	def PricVal(self):
		return self._PricVal

	@PricVal.setter
	def PricVal(self, value):
		self._PricVal = value if value is not None else base_types.UninitialisedField(self, 'PricVal', Percentage14Rate, False)

	@PricVal.deleter
	def PricVal(self):
		del self._PricVal
		self._PricVal = base_types.UninitialisedField(self, 'PricVal', Percentage14Rate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PctgPricTp', type=PriceRateType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricVal', type=Percentage14Rate, min=1, max=1, mutex_group=None, array=False),
	))