from . import base_types
from ._SupplementaryData1 import SupplementaryData1
from ._MessageHeader1 import MessageHeader1
from ._SecurityCSDLink12 import SecurityCSDLink12

class SecurityCSDLinkCreationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_SctyCSDLk", "_MsgHdr"]
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
	def SctyCSDLk(self):
		return self._SctyCSDLk

	@SctyCSDLk.setter
	def SctyCSDLk(self, value):
		self._SctyCSDLk = value if type(value) != base_types.auto else self.make_default("SctyCSDLk")

	@SctyCSDLk.deleter
	def SctyCSDLk(self):
		del self._SctyCSDLk
		self._SctyCSDLk = None

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
		base_types.FieldEntry(name='SctyCSDLk', type=SecurityCSDLink12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
	))

