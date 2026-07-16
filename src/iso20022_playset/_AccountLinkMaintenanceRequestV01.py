# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountLink8
from . import AccountLinkUpdate2
from . import MessageHeader1
from . import SupplementaryData1

class AccountLinkMaintenanceRequestV01(base_types._BaseFieldType):

	__slots__ = ["_AcctLkId", "_MsgHdr", "_SplmtryData", "_Upd"]
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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if value is not None else base_types.UninitialisedField(self, 'Upd', AccountLinkUpdate2, False)

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = base_types.UninitialisedField(self, 'Upd', AccountLinkUpdate2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctLkId', type=AccountLink8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Upd', type=AccountLinkUpdate2, min=1, max=1, mutex_group=None, array=False),
	))