from . import base_types
from .RestrictedFINMax15Text import RestrictedFINMax15Text
from .ProtectInstructionStatus4Code import ProtectInstructionStatus4Code
from .ISODate import ISODate
from .ProtectTransactionType3Code import ProtectTransactionType3Code
from .FinancialInstrumentQuantity31Choice import FinancialInstrumentQuantity31Choice

class ProtectInstruction8(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_UcvrdPrtctQty", "_TxTp", "_PrtctDt", "_PrtctTxSts"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def UcvrdPrtctQty(self):
		return self._UcvrdPrtctQty

	@UcvrdPrtctQty.setter
	def UcvrdPrtctQty(self, value):
		self._UcvrdPrtctQty = value if type(value) != base_types.auto else self.make_default("UcvrdPrtctQty")

	@UcvrdPrtctQty.deleter
	def UcvrdPrtctQty(self):
		del self._UcvrdPrtctQty
		self._UcvrdPrtctQty = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != base_types.auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if type(value) != base_types.auto else self.make_default("PrtctDt")

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = None

	@property
	def PrtctTxSts(self):
		return self._PrtctTxSts

	@PrtctTxSts.setter
	def PrtctTxSts(self, value):
		self._PrtctTxSts = value if type(value) != base_types.auto else self.make_default("PrtctTxSts")

	@PrtctTxSts.deleter
	def PrtctTxSts(self):
		del self._PrtctTxSts
		self._PrtctTxSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=RestrictedFINMax15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcvrdPrtctQty', type=FinancialInstrumentQuantity31Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ProtectTransactionType3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctTxSts', type=ProtectInstructionStatus4Code, min=0, max=1, mutex_group=None, array=False),
	))

