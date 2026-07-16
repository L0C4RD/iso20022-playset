# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max16Text

class GeographicCoordinates1(base_types._BaseFieldType):

	__slots__ = ["_Lat", "_Long"]
	@property
	def Lat(self):
		return self._Lat

	@Lat.setter
	def Lat(self, value):
		self._Lat = value if value is not None else base_types.UninitialisedField(self, 'Lat', Max16Text, False)

	@Lat.deleter
	def Lat(self):
		del self._Lat
		self._Lat = base_types.UninitialisedField(self, 'Lat', Max16Text, False)

	@property
	def Long(self):
		return self._Long

	@Long.setter
	def Long(self, value):
		self._Long = value if value is not None else base_types.UninitialisedField(self, 'Long', Max16Text, False)

	@Long.deleter
	def Long(self):
		del self._Long
		self._Long = base_types.UninitialisedField(self, 'Long', Max16Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lat', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Long', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
	))