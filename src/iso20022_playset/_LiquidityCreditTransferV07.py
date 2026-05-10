from . import base_types
from ._LiquidityCreditTransfer4 import LiquidityCreditTransfer4
from ._MessageHeader1 import MessageHeader1
from ._SupplementaryData1 import SupplementaryData1

class LiquidityCreditTransferV07(base_types._BaseFieldType):

	__slots__ = ["_LqdtyCdtTrf", "_MsgHdr", "_SplmtryData"]
	@property
	def LqdtyCdtTrf(self):
		return self._LqdtyCdtTrf

	@LqdtyCdtTrf.setter
	def LqdtyCdtTrf(self, value):
		self._LqdtyCdtTrf = value if type(value) != base_types.auto else self.make_default("LqdtyCdtTrf")

	@LqdtyCdtTrf.deleter
	def LqdtyCdtTrf(self):
		del self._LqdtyCdtTrf
		self._LqdtyCdtTrf = None

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
		base_types.FieldEntry(name='LqdtyCdtTrf', type=LiquidityCreditTransfer4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

