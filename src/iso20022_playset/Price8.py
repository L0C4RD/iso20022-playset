import base_types
import TypeOfPrice1Code
import PriceValueType3Code
import PriceRateOrAmount3Choice

class Price8(base_types._BaseFieldType):

	__slots__ = ["_PricTp", "_ValTp", "_Val"]
	@property
	def PricTp(self):
		return self._PricTp

	@PricTp.setter
	def PricTp(self, value):
		self._PricTp = value if type(value) != auto else self.make_default("PricTp")

	@PricTp.deleter
	def PricTp(self):
		del self._PricTp
		self._PricTp = None

	@property
	def ValTp(self):
		return self._ValTp

	@ValTp.setter
	def ValTp(self, value):
		self._ValTp = value if type(value) != auto else self.make_default("ValTp")

	@ValTp.deleter
	def ValTp(self):
		del self._ValTp
		self._ValTp = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PricTp', type=TypeOfPrice1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValTp', type=PriceValueType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PriceRateOrAmount3Choice, min=1, max=1, mutex_group=None, array=False),
	))

