# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceMethod1Code
from . import PriceValue1
from . import UnitPriceType2Choice

class UnitPrice20(base_types._BaseFieldType):

	__slots__ = ["_PricMtd", "_PricTp", "_Val"]
	@property
	def PricMtd(self):
		return self._PricMtd

	@PricMtd.setter
	def PricMtd(self, value):
		self._PricMtd = value if value is not None else base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@PricMtd.deleter
	def PricMtd(self):
		del self._PricMtd
		self._PricMtd = base_types.UninitialisedField(self, 'PricMtd', PriceMethod1Code, False)

	@property
	def PricTp(self):
		return self._PricTp

	@PricTp.setter
	def PricTp(self, value):
		self._PricTp = value if value is not None else base_types.UninitialisedField(self, 'PricTp', UnitPriceType2Choice, False)

	@PricTp.deleter
	def PricTp(self):
		del self._PricTp
		self._PricTp = base_types.UninitialisedField(self, 'PricTp', UnitPriceType2Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PriceValue1, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PriceValue1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricMtd', type=PriceMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTp', type=UnitPriceType2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceValue1, min=1, max=1, mutex_group=None, array=False),
	))