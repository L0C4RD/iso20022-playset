# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader9
from . import SupplementaryData1
from . import TransactionQuery8

class GetTransactionV11(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_SplmtryData", "_TxQryDef"]
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

	@property
	def TxQryDef(self):
		return self._TxQryDef

	@TxQryDef.setter
	def TxQryDef(self, value):
		self._TxQryDef = value if value is not None else base_types.UninitialisedField(self, 'TxQryDef', TransactionQuery8, False)

	@TxQryDef.deleter
	def TxQryDef(self):
		del self._TxQryDef
		self._TxQryDef = base_types.UninitialisedField(self, 'TxQryDef', TransactionQuery8, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxQryDef', type=TransactionQuery8, min=0, max=1, mutex_group=None, array=False),
	))