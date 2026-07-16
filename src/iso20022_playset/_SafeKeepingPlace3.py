# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LEIIdentifier
from . import SafekeepingPlaceFormat29Choice

class SafeKeepingPlace3(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_SfkpgPlcFrmt"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if value is not None else base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = base_types.UninitialisedField(self, 'LEI', LEIIdentifier, False)

	@property
	def SfkpgPlcFrmt(self):
		return self._SfkpgPlcFrmt

	@SfkpgPlcFrmt.setter
	def SfkpgPlcFrmt(self, value):
		self._SfkpgPlcFrmt = value if value is not None else base_types.UninitialisedField(self, 'SfkpgPlcFrmt', SafekeepingPlaceFormat29Choice, False)

	@SfkpgPlcFrmt.deleter
	def SfkpgPlcFrmt(self):
		del self._SfkpgPlcFrmt
		self._SfkpgPlcFrmt = base_types.UninitialisedField(self, 'SfkpgPlcFrmt', SafekeepingPlaceFormat29Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SfkpgPlcFrmt', type=SafekeepingPlaceFormat29Choice, min=0, max=1, mutex_group=None, array=False),
	))