# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity18Choice
from . import ISODate
from . import Max15Text
from . import Max35Text
from . import ProtectInstructionStatus3Code
from . import ProtectTransactionType2Code

class ProtectInstruction2(base_types._BaseFieldType):

	__slots__ = ["_PrtctDt", "_PrtctSfkpgAcct", "_PrtctTxSts", "_TxId", "_TxTp", "_UcvrdPrtctQty"]
	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if value is not None else base_types.UninitialisedField(self, 'PrtctDt', ISODate, False)

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = base_types.UninitialisedField(self, 'PrtctDt', ISODate, False)

	@property
	def PrtctSfkpgAcct(self):
		return self._PrtctSfkpgAcct

	@PrtctSfkpgAcct.setter
	def PrtctSfkpgAcct(self, value):
		self._PrtctSfkpgAcct = value if value is not None else base_types.UninitialisedField(self, 'PrtctSfkpgAcct', Max35Text, False)

	@PrtctSfkpgAcct.deleter
	def PrtctSfkpgAcct(self):
		del self._PrtctSfkpgAcct
		self._PrtctSfkpgAcct = base_types.UninitialisedField(self, 'PrtctSfkpgAcct', Max35Text, False)

	@property
	def PrtctTxSts(self):
		return self._PrtctTxSts

	@PrtctTxSts.setter
	def PrtctTxSts(self, value):
		self._PrtctTxSts = value if value is not None else base_types.UninitialisedField(self, 'PrtctTxSts', ProtectInstructionStatus3Code, False)

	@PrtctTxSts.deleter
	def PrtctTxSts(self):
		del self._PrtctTxSts
		self._PrtctTxSts = base_types.UninitialisedField(self, 'PrtctTxSts', ProtectInstructionStatus3Code, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max15Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max15Text, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', ProtectTransactionType2Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', ProtectTransactionType2Code, False)

	@property
	def UcvrdPrtctQty(self):
		return self._UcvrdPrtctQty

	@UcvrdPrtctQty.setter
	def UcvrdPrtctQty(self, value):
		self._UcvrdPrtctQty = value if value is not None else base_types.UninitialisedField(self, 'UcvrdPrtctQty', FinancialInstrumentQuantity18Choice, False)

	@UcvrdPrtctQty.deleter
	def UcvrdPrtctQty(self):
		del self._UcvrdPrtctQty
		self._UcvrdPrtctQty = base_types.UninitialisedField(self, 'UcvrdPrtctQty', FinancialInstrumentQuantity18Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctSfkpgAcct', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctTxSts', type=ProtectInstructionStatus3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ProtectTransactionType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcvrdPrtctQty', type=FinancialInstrumentQuantity18Choice, min=0, max=1, mutex_group=None, array=False),
	))