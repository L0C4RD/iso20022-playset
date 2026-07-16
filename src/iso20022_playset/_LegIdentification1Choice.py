# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class LegIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_RedLegId", "_SbcptLegId"]
	@property
	def RedLegId(self):
		return self._RedLegId

	@RedLegId.setter
	def RedLegId(self, value):
		self._RedLegId = value if value is not None else base_types.UninitialisedField(self, 'RedLegId', Max35Text, False)

	@RedLegId.deleter
	def RedLegId(self):
		del self._RedLegId
		self._RedLegId = base_types.UninitialisedField(self, 'RedLegId', Max35Text, False)

	@property
	def SbcptLegId(self):
		return self._SbcptLegId

	@SbcptLegId.setter
	def SbcptLegId(self, value):
		self._SbcptLegId = value if value is not None else base_types.UninitialisedField(self, 'SbcptLegId', Max35Text, False)

	@SbcptLegId.deleter
	def SbcptLegId(self):
		del self._SbcptLegId
		self._SbcptLegId = base_types.UninitialisedField(self, 'SbcptLegId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RedLegId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SbcptLegId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))