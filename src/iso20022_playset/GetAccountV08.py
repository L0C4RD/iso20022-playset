from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .AccountQuery4 import AccountQuery4
from .MessageHeader9 import MessageHeader9

class GetAccountV08(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MsgHdr", "_AcctQryDef"]
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
	def AcctQryDef(self):
		return self._AcctQryDef

	@AcctQryDef.setter
	def AcctQryDef(self, value):
		self._AcctQryDef = value if type(value) != base_types.auto else self.make_default("AcctQryDef")

	@AcctQryDef.deleter
	def AcctQryDef(self):
		del self._AcctQryDef
		self._AcctQryDef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctQryDef', type=AccountQuery4, min=0, max=1, mutex_group=None, array=False),
	))

