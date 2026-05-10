import base_types
import Max35Text
import ClearingSystemIdentification2Choice

class ClearingSystemMemberIdentification2(base_types._BaseFieldType):

	__slots__ = ["_ClrSysId", "_MmbId"]
	@property
	def ClrSysId(self):
		return self._ClrSysId

	@ClrSysId.setter
	def ClrSysId(self, value):
		self._ClrSysId = value if type(value) != auto else self.make_default("ClrSysId")

	@ClrSysId.deleter
	def ClrSysId(self):
		del self._ClrSysId
		self._ClrSysId = None

	@property
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if type(value) != auto else self.make_default("MmbId")

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSysId', type=ClearingSystemIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

