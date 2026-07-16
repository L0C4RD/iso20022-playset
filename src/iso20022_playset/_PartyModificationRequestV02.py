# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader1
from . import SupplementaryData1
from . import SystemPartyIdentification8
from . import SystemPartyModification3

class PartyModificationRequestV02(base_types._BaseFieldType):

	__slots__ = ["_Mod", "_MsgHdr", "_SplmtryData", "_SysPtyId"]
	@property
	def Mod(self):
		return self._Mod

	@Mod.setter
	def Mod(self, value):
		self._Mod = value if value is not None else base_types.UninitialisedField(self, 'Mod', SystemPartyModification3, True)

	@Mod.deleter
	def Mod(self):
		del self._Mod
		self._Mod = base_types.UninitialisedField(self, 'Mod', SystemPartyModification3, True)

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def SysPtyId(self):
		return self._SysPtyId

	@SysPtyId.setter
	def SysPtyId(self, value):
		self._SysPtyId = value if value is not None else base_types.UninitialisedField(self, 'SysPtyId', SystemPartyIdentification8, False)

	@SysPtyId.deleter
	def SysPtyId(self):
		del self._SysPtyId
		self._SysPtyId = base_types.UninitialisedField(self, 'SysPtyId', SystemPartyIdentification8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mod', type=SystemPartyModification3, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SysPtyId', type=SystemPartyIdentification8, min=1, max=1, mutex_group=None, array=False),
	))