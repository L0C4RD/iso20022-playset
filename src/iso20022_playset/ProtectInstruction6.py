import base_types
import ProtectTransactionType2Code
import FinancialInstrumentQuantity31Choice
import ISODate
import RestrictedFINMax15Text
import ProtectInstructionStatus3Code
import RestrictedFINMax35Text

class ProtectInstruction6(base_types._BaseFieldType):

	__slots__ = ["_UcvrdPrtctQty", "_PrtctDt", "_PrtctSfkpgAcct", "_TxTp", "_TxId", "_PrtctTxSts"]
	@property
	def UcvrdPrtctQty(self):
		return self._UcvrdPrtctQty

	@UcvrdPrtctQty.setter
	def UcvrdPrtctQty(self, value):
		self._UcvrdPrtctQty = value if type(value) != auto else self.make_default("UcvrdPrtctQty")

	@UcvrdPrtctQty.deleter
	def UcvrdPrtctQty(self):
		del self._UcvrdPrtctQty
		self._UcvrdPrtctQty = None

	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if type(value) != auto else self.make_default("PrtctDt")

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = None

	@property
	def PrtctSfkpgAcct(self):
		return self._PrtctSfkpgAcct

	@PrtctSfkpgAcct.setter
	def PrtctSfkpgAcct(self, value):
		self._PrtctSfkpgAcct = value if type(value) != auto else self.make_default("PrtctSfkpgAcct")

	@PrtctSfkpgAcct.deleter
	def PrtctSfkpgAcct(self):
		del self._PrtctSfkpgAcct
		self._PrtctSfkpgAcct = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def PrtctTxSts(self):
		return self._PrtctTxSts

	@PrtctTxSts.setter
	def PrtctTxSts(self, value):
		self._PrtctTxSts = value if type(value) != auto else self.make_default("PrtctTxSts")

	@PrtctTxSts.deleter
	def PrtctTxSts(self):
		del self._PrtctTxSts
		self._PrtctTxSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UcvrdPrtctQty', type=FinancialInstrumentQuantity31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctSfkpgAcct', type=RestrictedFINMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ProtectTransactionType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=RestrictedFINMax15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctTxSts', type=ProtectInstructionStatus3Code, min=0, max=1, mutex_group=None, array=False),
	))

