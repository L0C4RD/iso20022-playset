# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ResponseStatus6Choice
from . import SupplementaryData1
from . import TransactionDetails183
from . import TransactionIdentification6

class SecuritiesSettlementTransactionCounterpartyResponseV06(base_types._BaseFieldType):

	__slots__ = ["_RspnSts", "_SplmtryData", "_TxDtls", "_TxId"]
	@property
	def RspnSts(self):
		return self._RspnSts

	@RspnSts.setter
	def RspnSts(self, value):
		self._RspnSts = value if value is not None else base_types.UninitialisedField(self, 'RspnSts', ResponseStatus6Choice, False)

	@RspnSts.deleter
	def RspnSts(self):
		del self._RspnSts
		self._RspnSts = base_types.UninitialisedField(self, 'RspnSts', ResponseStatus6Choice, False)

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
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', TransactionDetails183, False)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', TransactionDetails183, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', TransactionIdentification6, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', TransactionIdentification6, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnSts', type=ResponseStatus6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxDtls', type=TransactionDetails183, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentification6, min=1, max=1, mutex_group=None, array=False),
	))