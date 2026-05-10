import base_types
import SupplementaryData1
import MessageHeader12
import AccountLinkStatus1
import AccountLink8

class AccountLinkStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AcctLkSts", "_SplmtryData", "_MsgHdr", "_AcctLkId"]
	@property
	def AcctLkSts(self):
		return self._AcctLkSts

	@AcctLkSts.setter
	def AcctLkSts(self, value):
		self._AcctLkSts = value if type(value) != auto else self.make_default("AcctLkSts")

	@AcctLkSts.deleter
	def AcctLkSts(self):
		del self._AcctLkSts
		self._AcctLkSts = None

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
	def AcctLkId(self):
		return self._AcctLkId

	@AcctLkId.setter
	def AcctLkId(self, value):
		self._AcctLkId = value if type(value) != auto else self.make_default("AcctLkId")

	@AcctLkId.deleter
	def AcctLkId(self):
		del self._AcctLkId
		self._AcctLkId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctLkSts', type=AccountLinkStatus1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctLkId', type=AccountLink8, min=0, max=1, mutex_group=None, array=False),
	))

