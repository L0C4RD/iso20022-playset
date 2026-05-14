# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BICFIDec2014Identifier import BICFIDec2014Identifier
from ._BranchData2 import BranchData2
from ._ClearingSystemMemberIdentification4Choice import ClearingSystemMemberIdentification4Choice
from ._LEIIdentifier import LEIIdentifier
from ._Max35Text import Max35Text
from ._NameAndAddress5 import NameAndAddress5

class FinancialInstitutionIdentification16(base_types._BaseFieldType):

	__slots__ = ["_BICFI", "_BrnchId", "_ClrSysMmbId", "_LEI", "_NmAndAdr", "_PrtryId"]
	@property
	def BICFI(self):
		return self._BICFI

	@BICFI.setter
	def BICFI(self, value):
		self._BICFI = value if type(value) != base_types.auto else self.make_default("BICFI")

	@BICFI.deleter
	def BICFI(self):
		del self._BICFI
		self._BICFI = None

	@property
	def BrnchId(self):
		return self._BrnchId

	@BrnchId.setter
	def BrnchId(self, value):
		self._BrnchId = value if type(value) != base_types.auto else self.make_default("BrnchId")

	@BrnchId.deleter
	def BrnchId(self):
		del self._BrnchId
		self._BrnchId = None

	@property
	def ClrSysMmbId(self):
		return self._ClrSysMmbId

	@ClrSysMmbId.setter
	def ClrSysMmbId(self, value):
		self._ClrSysMmbId = value if type(value) != base_types.auto else self.make_default("ClrSysMmbId")

	@ClrSysMmbId.deleter
	def ClrSysMmbId(self):
		del self._ClrSysMmbId
		self._ClrSysMmbId = None

	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def NmAndAdr(self):
		return self._NmAndAdr

	@NmAndAdr.setter
	def NmAndAdr(self, value):
		self._NmAndAdr = value if type(value) != base_types.auto else self.make_default("NmAndAdr")

	@NmAndAdr.deleter
	def NmAndAdr(self):
		del self._NmAndAdr
		self._NmAndAdr = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BICFI', type=BICFIDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrnchId', type=BranchData2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSysMmbId', type=ClearingSystemMemberIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmAndAdr', type=NameAndAddress5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))