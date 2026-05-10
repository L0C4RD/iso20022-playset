import base_types
import PercentageRate
import PriceRateType3FormatChoice

class PriceRate1(base_types._BaseFieldType):

	__slots__ = ["_RateTp", "_Rate"]
	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateTp', type=PriceRateType3FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))

