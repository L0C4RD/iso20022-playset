from . import base_types
from ._EligibleSecurity5 import EligibleSecurity5
from ._MessageHeader1 import MessageHeader1
from ._SupplementaryData1 import SupplementaryData1

class EligibleSecuritiesDeletionRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ElgblScty", "_MsgHdr", "_SplmtryData"]
	@property
	def ElgblScty(self):
		return self._ElgblScty

	@ElgblScty.setter
	def ElgblScty(self, value):
		self._ElgblScty = value if type(value) != base_types.auto else self.make_default("ElgblScty")

	@ElgblScty.deleter
	def ElgblScty(self):
		del self._ElgblScty
		self._ElgblScty = None

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
		base_types.FieldEntry(name='ElgblScty', type=EligibleSecurity5, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

