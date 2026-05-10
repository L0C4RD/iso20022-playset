from . import base_types
from .UTMCoordinates1 import UTMCoordinates1
from .GeographicCoordinates1 import GeographicCoordinates1

class GeographicLocation1Choice(base_types._BaseFieldType):

	__slots__ = ["_GeogcCordints", "_UTMCordints"]
	@property
	def GeogcCordints(self):
		return self._GeogcCordints

	@GeogcCordints.setter
	def GeogcCordints(self, value):
		self._GeogcCordints = value if type(value) != base_types.auto else self.make_default("GeogcCordints")

	@GeogcCordints.deleter
	def GeogcCordints(self):
		del self._GeogcCordints
		self._GeogcCordints = None

	@property
	def UTMCordints(self):
		return self._UTMCordints

	@UTMCordints.setter
	def UTMCordints(self, value):
		self._UTMCordints = value if type(value) != base_types.auto else self.make_default("UTMCordints")

	@UTMCordints.deleter
	def UTMCordints(self):
		del self._UTMCordints
		self._UTMCordints = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='GeogcCordints', type=GeographicCoordinates1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UTMCordints', type=UTMCoordinates1, min=0, max=1, mutex_group=1, array=False),
	))

