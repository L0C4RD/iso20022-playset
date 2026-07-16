# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MemberIdentification3Choice
from . import SystemIdentification2Choice

class SystemMember3(base_types._BaseFieldType):

	__slots__ = ["_MmbId", "_SysId"]
	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if value is not None else base_types.UninitialisedField(self, 'MmbId', MemberIdentification3Choice, False)

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = base_types.UninitialisedField(self, 'MmbId', MemberIdentification3Choice, False)

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if value is not None else base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MmbId', type=MemberIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))