from . import base_types
from .PercentageRate import PercentageRate
from .ExternalRelativeTo1Code import ExternalRelativeTo1Code

class Percentage1(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_RltvTo"]
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
	def RltvTo(self):
		return self._RltvTo

	@RltvTo.setter
	def RltvTo(self, value):
		self._RltvTo = value if type(value) != base_types.auto else self.make_default("RltvTo")

	@RltvTo.deleter
	def RltvTo(self):
		del self._RltvTo
		self._RltvTo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltvTo', type=ExternalRelativeTo1Code, min=1, max=1, mutex_group=None, array=False),
	))

