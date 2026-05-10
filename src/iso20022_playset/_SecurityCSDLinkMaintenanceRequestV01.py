from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .MessageHeader1 import MessageHeader1
from .SecurityCSDLinkUpdate3 import SecurityCSDLinkUpdate3
from .SecurityCSDLink9 import SecurityCSDLink9

class SecurityCSDLinkMaintenanceRequestV01(base_types._BaseFieldType):

	__slots__ = ["_SctyCSDLkId", "_SplmtryData", "_Upd", "_MsgHdr"]
	@property
	def SctyCSDLkId(self):
		return self._SctyCSDLkId

	@SctyCSDLkId.setter
	def SctyCSDLkId(self, value):
		self._SctyCSDLkId = value if type(value) != base_types.auto else self.make_default("SctyCSDLkId")

	@SctyCSDLkId.deleter
	def SctyCSDLkId(self):
		del self._SctyCSDLkId
		self._SctyCSDLkId = None

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
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if type(value) != base_types.auto else self.make_default("Upd")

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = None

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
		base_types.FieldEntry(name='SctyCSDLkId', type=SecurityCSDLink9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Upd', type=SecurityCSDLinkUpdate3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
	))

