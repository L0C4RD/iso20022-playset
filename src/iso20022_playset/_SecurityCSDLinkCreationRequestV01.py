# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader1
from . import SecurityCSDLink12
from . import SupplementaryData1

class SecurityCSDLinkCreationRequestV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SctyCSDLk", "_SplmtryData"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@property
	def SctyCSDLk(self):
		return self._SctyCSDLk

	@SctyCSDLk.setter
	def SctyCSDLk(self, value):
		self._SctyCSDLk = value if value is not None else base_types.UninitialisedField(self, 'SctyCSDLk', SecurityCSDLink12, True)

	@SctyCSDLk.deleter
	def SctyCSDLk(self):
		del self._SctyCSDLk
		self._SctyCSDLk = base_types.UninitialisedField(self, 'SctyCSDLk', SecurityCSDLink12, True)

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyCSDLk', type=SecurityCSDLink12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))