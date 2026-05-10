from . import base_types
from .SkipPayload import SkipPayload

class ProprietaryData6(base_types._BaseFieldType):

	__slots__ = ["_Any"]
	@property
	def Any(self):
		return self._Any

	@Any.setter
	def Any(self, value):
		self._Any = value if type(value) != auto else self.make_default("Any")

	@Any.deleter
	def Any(self):
		del self._Any
		self._Any = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Any', type=SkipPayload, min=1, max=1, mutex_group=None, array=False),
	))

