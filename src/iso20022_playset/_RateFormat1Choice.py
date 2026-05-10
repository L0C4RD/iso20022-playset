from . import base_types
from .PercentageRate import PercentageRate
from .RateType12FormatChoice import RateType12FormatChoice

class RateFormat1Choice(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_NotSpcfdRate"]
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

	@property
	def NotSpcfdRate(self):
		return self._NotSpcfdRate

	@NotSpcfdRate.setter
	def NotSpcfdRate(self, value):
		self._NotSpcfdRate = value if type(value) != base_types.auto else self.make_default("NotSpcfdRate")

	@NotSpcfdRate.deleter
	def NotSpcfdRate(self):
		del self._NotSpcfdRate
		self._NotSpcfdRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdRate', type=RateType12FormatChoice, min=0, max=1, mutex_group=1, array=False),
	))

