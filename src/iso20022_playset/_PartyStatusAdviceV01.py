from . import base_types
from ._MessageHeader12 import MessageHeader12
from ._PartyStatus2 import PartyStatus2
from ._SupplementaryData1 import SupplementaryData1

class PartyStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_PtySts", "_SplmtryData"]
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
	def PtySts(self):
		return self._PtySts

	@PtySts.setter
	def PtySts(self, value):
		self._PtySts = value if type(value) != base_types.auto else self.make_default("PtySts")

	@PtySts.deleter
	def PtySts(self):
		del self._PtySts
		self._PtySts = None

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtySts', type=PartyStatus2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

