from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .MessageHeader9 import MessageHeader9
from .BusinessDayQuery2 import BusinessDayQuery2

class GetBusinessDayInformationV05(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_BizDayInfQryDef"]
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

	@property
	def BizDayInfQryDef(self):
		return self._BizDayInfQryDef

	@BizDayInfQryDef.setter
	def BizDayInfQryDef(self, value):
		self._BizDayInfQryDef = value if type(value) != base_types.auto else self.make_default("BizDayInfQryDef")

	@BizDayInfQryDef.deleter
	def BizDayInfQryDef(self):
		del self._BizDayInfQryDef
		self._BizDayInfQryDef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BizDayInfQryDef', type=BusinessDayQuery2, min=0, max=1, mutex_group=None, array=False),
	))

