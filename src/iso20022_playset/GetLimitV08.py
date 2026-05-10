import base_types
import LimitQuery5
import SupplementaryData1
import MessageHeader9

class GetLimitV08(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_LmtQryDef"]
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
	def LmtQryDef(self):
		return self._LmtQryDef

	@LmtQryDef.setter
	def LmtQryDef(self, value):
		self._LmtQryDef = value if type(value) != auto else self.make_default("LmtQryDef")

	@LmtQryDef.deleter
	def LmtQryDef(self):
		del self._LmtQryDef
		self._LmtQryDef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LmtQryDef', type=LimitQuery5, min=0, max=1, mutex_group=None, array=False),
	))

