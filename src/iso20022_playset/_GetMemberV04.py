from . import base_types
from ._MemberQueryDefinition4 import MemberQueryDefinition4
from ._MessageHeader9 import MessageHeader9
from ._SupplementaryData1 import SupplementaryData1

class GetMemberV04(base_types._BaseFieldType):

	__slots__ = ["_MmbQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def MmbQryDef(self):
		return self._MmbQryDef

	@MmbQryDef.setter
	def MmbQryDef(self, value):
		self._MmbQryDef = value if type(value) != base_types.auto else self.make_default("MmbQryDef")

	@MmbQryDef.deleter
	def MmbQryDef(self):
		del self._MmbQryDef
		self._MmbQryDef = None

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if type(value) != base_types.auto else self.make_default("MsgHdr")

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MmbQryDef', type=MemberQueryDefinition4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

