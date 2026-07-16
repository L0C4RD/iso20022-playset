# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountQuery4
from . import MessageHeader9
from . import SupplementaryData1

class GetAccountV08(base_types._BaseFieldType):

	__slots__ = ["_AcctQryDef", "_MsgHdr", "_SplmtryData"]
	@property
	def AcctQryDef(self):
		return self._AcctQryDef

	@AcctQryDef.setter
	def AcctQryDef(self, value):
		self._AcctQryDef = value if value is not None else base_types.UninitialisedField(self, 'AcctQryDef', AccountQuery4, False)

	@AcctQryDef.deleter
	def AcctQryDef(self):
		del self._AcctQryDef
		self._AcctQryDef = base_types.UninitialisedField(self, 'AcctQryDef', AccountQuery4, False)

	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader9, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader9, False)

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
		base_types.FieldEntry(name='AcctQryDef', type=AccountQuery4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))