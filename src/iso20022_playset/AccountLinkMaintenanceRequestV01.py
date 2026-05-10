from . import base_types
from .AccountLinkUpdate2 import AccountLinkUpdate2
from .AccountLink8 import AccountLink8
from .SupplementaryData1 import SupplementaryData1
from .MessageHeader1 import MessageHeader1

class AccountLinkMaintenanceRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AcctLkId", "_MsgHdr", "_SplmtryData", "_Upd"]
	@property
	def AcctLkId(self):
		return self._AcctLkId

	@AcctLkId.setter
	def AcctLkId(self, value):
		self._AcctLkId = value if type(value) != auto else self.make_default("AcctLkId")

	@AcctLkId.deleter
	def AcctLkId(self):
		del self._AcctLkId
		self._AcctLkId = None

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
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if type(value) != auto else self.make_default("Upd")

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctLkId', type=AccountLink8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Upd', type=AccountLinkUpdate2, min=1, max=1, mutex_group=None, array=False),
	))

