# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountLink8
from . import AccountLinkStatus1
from . import MessageHeader12
from . import SupplementaryData1

class AccountLinkStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_AcctLkId", "_AcctLkSts", "_MsgHdr", "_SplmtryData"]
	@property
	def AcctLkId(self):
		return self._AcctLkId

	@AcctLkId.setter
	def AcctLkId(self, value):
		self._AcctLkId = value if value is not None else base_types.UninitialisedField(self, 'AcctLkId', AccountLink8, False)

	@AcctLkId.deleter
	def AcctLkId(self):
		del self._AcctLkId
		self._AcctLkId = base_types.UninitialisedField(self, 'AcctLkId', AccountLink8, False)

	@property
	def AcctLkSts(self):
		return self._AcctLkSts

	@AcctLkSts.setter
	def AcctLkSts(self, value):
		self._AcctLkSts = value if value is not None else base_types.UninitialisedField(self, 'AcctLkSts', AccountLinkStatus1, False)

	@AcctLkSts.deleter
	def AcctLkSts(self):
		del self._AcctLkSts
		self._AcctLkSts = base_types.UninitialisedField(self, 'AcctLkSts', AccountLinkStatus1, False)

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
		base_types.FieldEntry(name='AcctLkId', type=AccountLink8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctLkSts', type=AccountLinkStatus1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))