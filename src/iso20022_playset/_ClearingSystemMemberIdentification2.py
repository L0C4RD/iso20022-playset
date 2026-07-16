# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClearingSystemIdentification2Choice
from . import Max35Text

class ClearingSystemMemberIdentification2(base_types._BaseFieldType):

	__slots__ = ["_ClrSysId", "_MmbId"]
	@property
	def ClrSysId(self):
		return self._ClrSysId

	@ClrSysId.setter
	def ClrSysId(self, value):
		self._ClrSysId = value if value is not None else base_types.UninitialisedField(self, 'ClrSysId', ClearingSystemIdentification2Choice, False)

	@ClrSysId.deleter
	def ClrSysId(self):
		del self._ClrSysId
		self._ClrSysId = base_types.UninitialisedField(self, 'ClrSysId', ClearingSystemIdentification2Choice, False)

	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if value is not None else base_types.UninitialisedField(self, 'MmbId', Max35Text, False)

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = base_types.UninitialisedField(self, 'MmbId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSysId', type=ClearingSystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))