from . import base_types
from .Max35Text import Max35Text

class GeolocationGeographicCoordinates1(base_types._BaseFieldType):

	__slots__ = ["_Lat", "_Long"]
	@property
	def Lat(self):
		return self._Lat

	@Lat.setter
	def Lat(self, value):
		self._Lat = value if type(value) != base_types.auto else self.make_default("Lat")

	@Lat.deleter
	def Lat(self):
		del self._Lat
		self._Lat = None

	@property
	def Long(self):
		return self._Long

	@Long.setter
	def Long(self, value):
		self._Long = value if type(value) != base_types.auto else self.make_default("Long")

	@Long.deleter
	def Long(self):
		del self._Long
		self._Long = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lat', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Long', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

