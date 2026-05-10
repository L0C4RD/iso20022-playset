import base_types
import ClearingSystemMemberIdentification4Choice
import BICFIDec2014Identifier
import Max35Text
import BranchData2
import NameAndAddress5
import LEIIdentifier

class FinancialInstitutionIdentification16(base_types._BaseFieldType):

	__slots__ = ["_ClrSysMmbId", "_LEI", "_BrnchId", "_PrtryId", "_BICFI", "_NmAndAdr"]
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
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if type(value) != auto else self.make_default("BrnchId")

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

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

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrSysMmbId', type=ClearingSystemMemberIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrnchId', type=BranchData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=None, array=False),
	))

