from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._PartyStatement3 import PartyStatement3
from ._MessageHeader1 import MessageHeader1

class PartyActivityAdviceV02(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_PtyActvty", "_MsgHdr"]
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
	def PtyActvty(self):
		return self._PtyActvty

	@PtyActvty.setter
	def PtyActvty(self, value):
		self._PtyActvty = value if type(value) != base_types.auto else self.make_default("PtyActvty")

	@PtyActvty.deleter
	def PtyActvty(self):
		del self._PtyActvty
		self._PtyActvty = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyActvty', type=PartyStatement3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
	))

