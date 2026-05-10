from . import base_types
from .MessageHeader9 import MessageHeader9
from .SupplementaryData1 import SupplementaryData1
from .TransactionQuery8 import TransactionQuery8

class GetTransactionV11(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_MsgHdr", "_TxQryDef"]
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
	def TxQryDef(self):
		return self._TxQryDef

	@TxQryDef.setter
	def TxQryDef(self, value):
		self._TxQryDef = value if type(value) != auto else self.make_default("TxQryDef")

	@TxQryDef.deleter
	def TxQryDef(self):
		del self._TxQryDef
		self._TxQryDef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxQryDef', type=TransactionQuery8, min=0, max=1, mutex_group=None, array=False),
	))

