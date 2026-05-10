from . import base_types
from ._StressSize1Choice import StressSize1Choice
from ._GenericIdentification168 import GenericIdentification168

class StressedProduct1(base_types._BaseFieldType):

	__slots__ = ["_MaxStrssSz", "_MinStrssSz", "_Id"]
	@property
	def MaxStrssSz(self):
		return self._MaxStrssSz

	@MaxStrssSz.setter
	def MaxStrssSz(self, value):
		self._MaxStrssSz = value if type(value) != base_types.auto else self.make_default("MaxStrssSz")

	@MaxStrssSz.deleter
	def MaxStrssSz(self):
		del self._MaxStrssSz
		self._MaxStrssSz = None

	@property
	def MinStrssSz(self):
		return self._MinStrssSz

	@MinStrssSz.setter
	def MinStrssSz(self, value):
		self._MinStrssSz = value if type(value) != base_types.auto else self.make_default("MinStrssSz")

	@MinStrssSz.deleter
	def MinStrssSz(self):
		del self._MinStrssSz
		self._MinStrssSz = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxStrssSz', type=StressSize1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MinStrssSz', type=StressSize1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=GenericIdentification168, min=1, max=1, mutex_group=None, array=False),
	))

