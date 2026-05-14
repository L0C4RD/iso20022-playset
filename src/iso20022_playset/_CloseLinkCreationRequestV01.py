from . import base_types
from ._CloseLink5 import CloseLink5
from ._MessageHeader1 import MessageHeader1
from ._SupplementaryData1 import SupplementaryData1

class CloseLinkCreationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_ClsLk", "_MsgHdr", "_SplmtryData"]
	@property
	def ClsLk(self):
		return self._ClsLk

	@ClsLk.setter
	def ClsLk(self, value):
		self._ClsLk = value if type(value) != base_types.auto else self.make_default("ClsLk")

	@ClsLk.deleter
	def ClsLk(self):
		del self._ClsLk
		self._ClsLk = None

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
		base_types.FieldEntry(name='ClsLk', type=CloseLink5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

