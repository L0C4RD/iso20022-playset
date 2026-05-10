from . import base_types
from ._SecuritiesAccountStatus2 import SecuritiesAccountStatus2
from ._SupplementaryData1 import SupplementaryData1
from ._MessageHeader12 import MessageHeader12

class SecuritiesAccountStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_SctiesAcctSts"]
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
	def SctiesAcctSts(self):
		return self._SctiesAcctSts

	@SctiesAcctSts.setter
	def SctiesAcctSts(self, value):
		self._SctiesAcctSts = value if type(value) != base_types.auto else self.make_default("SctiesAcctSts")

	@SctiesAcctSts.deleter
	def SctiesAcctSts(self):
		del self._SctiesAcctSts
		self._SctiesAcctSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctiesAcctSts', type=SecuritiesAccountStatus2, min=1, max=1, mutex_group=None, array=False),
	))

