from . import base_types
from .GeolocationGeographicCoordinates1 import GeolocationGeographicCoordinates1
from .GeolocationUTMCoordinates1 import GeolocationUTMCoordinates1

class Geolocation1(base_types._BaseFieldType):

	__slots__ = ["_UTMCordints", "_GeogcCordints"]
	@property
	def UTMCordints(self):
		return self._UTMCordints

	@UTMCordints.setter
	def UTMCordints(self, value):
		self._UTMCordints = value if type(value) != auto else self.make_default("UTMCordints")

	@UTMCordints.deleter
	def UTMCordints(self):
		del self._UTMCordints
		self._UTMCordints = None

	@property
	def GeogcCordints(self):
		return self._GeogcCordints

	@GeogcCordints.setter
	def GeogcCordints(self, value):
		self._GeogcCordints = value if type(value) != auto else self.make_default("GeogcCordints")

	@GeogcCordints.deleter
	def GeogcCordints(self):
		del self._GeogcCordints
		self._GeogcCordints = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UTMCordints', type=GeolocationUTMCoordinates1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GeogcCordints', type=GeolocationGeographicCoordinates1, min=0, max=1, mutex_group=None, array=False),
	))

