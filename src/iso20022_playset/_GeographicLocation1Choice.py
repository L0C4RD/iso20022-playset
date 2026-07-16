# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GeographicCoordinates1
from . import UTMCoordinates1

class GeographicLocation1Choice(base_types._BaseFieldType):

	__slots__ = ["_GeogcCordints", "_UTMCordints"]
	@property
	def GeogcCordints(self):
		return self._GeogcCordints

	@GeogcCordints.setter
	def GeogcCordints(self, value):
		self._GeogcCordints = value if value is not None else base_types.UninitialisedField(self, 'GeogcCordints', GeographicCoordinates1, False)

	@GeogcCordints.deleter
	def GeogcCordints(self):
		del self._GeogcCordints
		self._GeogcCordints = base_types.UninitialisedField(self, 'GeogcCordints', GeographicCoordinates1, False)

	@property
	def UTMCordints(self):
		return self._UTMCordints

	@UTMCordints.setter
	def UTMCordints(self, value):
		self._UTMCordints = value if value is not None else base_types.UninitialisedField(self, 'UTMCordints', UTMCoordinates1, False)

	@UTMCordints.deleter
	def UTMCordints(self):
		del self._UTMCordints
		self._UTMCordints = base_types.UninitialisedField(self, 'UTMCordints', UTMCoordinates1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='GeogcCordints', type=GeographicCoordinates1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UTMCordints', type=UTMCoordinates1, min=0, max=1, mutex_group=1, array=False),
	))