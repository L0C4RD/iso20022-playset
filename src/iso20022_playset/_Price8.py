# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PriceRateOrAmount3Choice
from . import PriceValueType3Code
from . import TypeOfPrice1Code

class Price8(base_types._BaseFieldType):

	__slots__ = ["_PricTp", "_Val", "_ValTp"]
	@property
	def PricTp(self):
		return self._PricTp

	@PricTp.setter
	def PricTp(self, value):
		self._PricTp = value if value is not None else base_types.UninitialisedField(self, 'PricTp', TypeOfPrice1Code, False)

	@PricTp.deleter
	def PricTp(self):
		del self._PricTp
		self._PricTp = base_types.UninitialisedField(self, 'PricTp', TypeOfPrice1Code, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PriceRateOrAmount3Choice, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PriceRateOrAmount3Choice, False)

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if value is not None else base_types.UninitialisedField(self, 'ValTp', PriceValueType3Code, False)

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = base_types.UninitialisedField(self, 'ValTp', PriceValueType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricTp', type=TypeOfPrice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmount3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValTp', type=PriceValueType3Code, min=0, max=1, mutex_group=None, array=False),
	))