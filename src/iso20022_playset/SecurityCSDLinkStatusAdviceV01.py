from . import base_types
import SecurityCSDLink9
import SupplementaryData1
import CSDLinkStatus1
import MessageHeader12

class SecurityCSDLinkStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SctyCSDLkSts", "_SplmtryData", "_SctyCSDLkId", "_MsgHdr"]
	@property
	def SctyCSDLkSts(self):
		return self._SctyCSDLkSts

	@SctyCSDLkSts.setter
	def SctyCSDLkSts(self, value):
		self._SctyCSDLkSts = value if type(value) != auto else self.make_default("SctyCSDLkSts")

	@SctyCSDLkSts.deleter
	def SctyCSDLkSts(self):
		del self._SctyCSDLkSts
		self._SctyCSDLkSts = None

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
	def SctyCSDLkId(self):
		return self._SctyCSDLkId

	@SctyCSDLkId.setter
	def SctyCSDLkId(self, value):
		self._SctyCSDLkId = value if type(value) != auto else self.make_default("SctyCSDLkId")

	@SctyCSDLkId.deleter
	def SctyCSDLkId(self):
		del self._SctyCSDLkId
		self._SctyCSDLkId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyCSDLkSts', type=CSDLinkStatus1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyCSDLkId', type=SecurityCSDLink9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
	))

