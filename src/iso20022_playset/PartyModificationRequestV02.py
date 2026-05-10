from . import base_types
from .SystemPartyIdentification8 import SystemPartyIdentification8
from .SupplementaryData1 import SupplementaryData1
from .MessageHeader1 import MessageHeader1
from .SystemPartyModification3 import SystemPartyModification3

class PartyModificationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_SysPtyId", "_Mod"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def SysPtyId(self):
		return self._SysPtyId

	@SysPtyId.setter
	def SysPtyId(self, value):
		self._SysPtyId = value if type(value) != auto else self.make_default("SysPtyId")

	@SysPtyId.deleter
	def SysPtyId(self):
		del self._SysPtyId
		self._SysPtyId = None

	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if type(value) != auto else self.make_default("Mod")

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysPtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mod', type=SystemPartyModification3, min=1, max=None, mutex_group=None, array=True),
	))

