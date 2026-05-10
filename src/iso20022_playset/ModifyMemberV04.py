import base_types
import Member6
import SupplementaryData1
import MessageHeader1
import MemberIdentification3Choice

class ModifyMemberV04(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_MmbId", "_NewMmbValSet", "_SplmtryData"]
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
	def MmbId(self):
		return self._MmbId

	@MmbId.setter
	def MmbId(self, value):
		self._MmbId = value if type(value) != auto else self.make_default("MmbId")

	@MmbId.deleter
	def MmbId(self):
		del self._MmbId
		self._MmbId = None

	@property
	def NewMmbValSet(self):
		return self._NewMmbValSet

	@NewMmbValSet.setter
	def NewMmbValSet(self, value):
		self._NewMmbValSet = value if type(value) != auto else self.make_default("NewMmbValSet")

	@NewMmbValSet.deleter
	def NewMmbValSet(self):
		del self._NewMmbValSet
		self._NewMmbValSet = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbId', type=MemberIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewMmbValSet', type=Member6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

