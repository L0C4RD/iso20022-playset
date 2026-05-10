from . import base_types
from ._MaturityTerm2 import MaturityTerm2

class TimeToMaturityPeriod1(base_types._BaseFieldType):

	__slots__ = ["_Start", "_End"]
	@property
	def End(self):
		return self._End

	@End.setter
	def End(self, value):
		self._End = value if type(value) != base_types.auto else self.make_default("End")

	@End.deleter
	def End(self):
		del self._End
		self._End = None

	@property
	def Start(self):
		return self._Start

	@Start.setter
	def Start(self, value):
		self._Start = value if type(value) != base_types.auto else self.make_default("Start")

	@Start.deleter
	def Start(self):
		del self._Start
		self._Start = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='End', type=MaturityTerm2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Start', type=MaturityTerm2, min=0, max=1, mutex_group=None, array=False),
	))

