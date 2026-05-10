from . import base_types
from .BICFIDec2014Identifier import BICFIDec2014Identifier
from .ClearingSystemMemberIdentification2 import ClearingSystemMemberIdentification2
from .GenericFinancialIdentification1 import GenericFinancialIdentification1

class MemberIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_ClrSysMmbId", "_Othr", "_BICFI"]
	@property
	def ClrSysMmbId(self):
		return self._ClrSysMmbId

	@ClrSysMmbId.setter
	def ClrSysMmbId(self, value):
		self._ClrSysMmbId = value if type(value) != auto else self.make_default("ClrSysMmbId")

	@ClrSysMmbId.deleter
	def ClrSysMmbId(self):
		del self._ClrSysMmbId
		self._ClrSysMmbId = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if type(value) != auto else self.make_default("BICFI")

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSysMmbId', type=ClearingSystemMemberIdentification2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=GenericFinancialIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=1, array=False),
	))

