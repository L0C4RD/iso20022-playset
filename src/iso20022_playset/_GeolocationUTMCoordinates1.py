# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class GeolocationUTMCoordinates1(base_types._BaseFieldType):

	__slots__ = ["_UTMEstwrd", "_UTMNrthwrd", "_UTMZone"]
	@property
	def UTMEstwrd(self):
		return self._UTMEstwrd

	@UTMEstwrd.setter
	def UTMEstwrd(self, value):
		self._UTMEstwrd = value if value is not None else base_types.UninitialisedField(self, 'UTMEstwrd', Max35Text, False)

	@UTMEstwrd.deleter
	def UTMEstwrd(self):
		del self._UTMEstwrd
		self._UTMEstwrd = base_types.UninitialisedField(self, 'UTMEstwrd', Max35Text, False)

	@property
	def UTMNrthwrd(self):
		return self._UTMNrthwrd

	@UTMNrthwrd.setter
	def UTMNrthwrd(self, value):
		self._UTMNrthwrd = value if value is not None else base_types.UninitialisedField(self, 'UTMNrthwrd', Max35Text, False)

	@UTMNrthwrd.deleter
	def UTMNrthwrd(self):
		del self._UTMNrthwrd
		self._UTMNrthwrd = base_types.UninitialisedField(self, 'UTMNrthwrd', Max35Text, False)

	@property
	def UTMZone(self):
		return self._UTMZone

	@UTMZone.setter
	def UTMZone(self, value):
		self._UTMZone = value if value is not None else base_types.UninitialisedField(self, 'UTMZone', Max35Text, False)

	@UTMZone.deleter
	def UTMZone(self):
		del self._UTMZone
		self._UTMZone = base_types.UninitialisedField(self, 'UTMZone', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='UTMEstwrd', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UTMNrthwrd', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UTMZone', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))