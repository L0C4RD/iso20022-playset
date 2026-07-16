# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CSDLinkStatus1
from . import MessageHeader12
from . import SecurityCSDLink9
from . import SupplementaryData1

class SecurityCSDLinkStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SctyCSDLkId", "_SctyCSDLkSts", "_SplmtryData"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader12, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader12, False)

	@property
	def SctyCSDLkId(self):
		return self._SctyCSDLkId

	@SctyCSDLkId.setter
	def SctyCSDLkId(self, value):
		self._SctyCSDLkId = value if value is not None else base_types.UninitialisedField(self, 'SctyCSDLkId', SecurityCSDLink9, False)

	@SctyCSDLkId.deleter
	def SctyCSDLkId(self):
		del self._SctyCSDLkId
		self._SctyCSDLkId = base_types.UninitialisedField(self, 'SctyCSDLkId', SecurityCSDLink9, False)

	@property
	def SctyCSDLkSts(self):
		return self._SctyCSDLkSts

	@SctyCSDLkSts.setter
	def SctyCSDLkSts(self, value):
		self._SctyCSDLkSts = value if value is not None else base_types.UninitialisedField(self, 'SctyCSDLkSts', CSDLinkStatus1, False)

	@SctyCSDLkSts.deleter
	def SctyCSDLkSts(self):
		del self._SctyCSDLkSts
		self._SctyCSDLkSts = base_types.UninitialisedField(self, 'SctyCSDLkSts', CSDLinkStatus1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyCSDLkId', type=SecurityCSDLink9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyCSDLkSts', type=CSDLinkStatus1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))