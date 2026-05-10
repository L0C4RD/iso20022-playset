from . import base_types
from ._MemberIdentification3Choice import MemberIdentification3Choice
from ._SystemIdentification2Choice import SystemIdentification2Choice

class SystemMember3(base_types._BaseFieldType):

	__slots__ = ["_SysId", "_MmbId"]
	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if type(value) != base_types.auto else self.make_default("MmbId")

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != base_types.auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MmbId', type=MemberIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

