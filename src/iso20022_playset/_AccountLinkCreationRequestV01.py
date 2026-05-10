from . import base_types
from ._AccountLink7 import AccountLink7
from ._MessageHeader1 import MessageHeader1
from ._SupplementaryData1 import SupplementaryData1

class AccountLinkCreationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AcctLk", "_MsgHdr", "_SplmtryData"]
	@property
	def AcctLk(self):
		return self._AcctLk

	@AcctLk.setter
	def AcctLk(self, value):
		self._AcctLk = value if type(value) != base_types.auto else self.make_default("AcctLk")

	@AcctLk.deleter
	def AcctLk(self):
		del self._AcctLk
		self._AcctLk = None

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
		base_types.FieldEntry(name='AcctLk', type=AccountLink7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

