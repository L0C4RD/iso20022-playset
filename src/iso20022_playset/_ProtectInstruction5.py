from . import base_types
from .RestrictedFINMax35Text import RestrictedFINMax35Text
from .ProtectTransactionType2Code import ProtectTransactionType2Code
from .RestrictedFINMax15Text import RestrictedFINMax15Text
from .ISODate import ISODate

class ProtectInstruction5(base_types._BaseFieldType):

	__slots__ = ["_PrtctSfkpgAcct", "_TxId", "_TxTp", "_PrtctDt"]
	@property
	def PrtctSfkpgAcct(self):
		return self._PrtctSfkpgAcct

	@PrtctSfkpgAcct.setter
	def PrtctSfkpgAcct(self, value):
		self._PrtctSfkpgAcct = value if type(value) != base_types.auto else self.make_default("PrtctSfkpgAcct")

	@PrtctSfkpgAcct.deleter
	def PrtctSfkpgAcct(self):
		del self._PrtctSfkpgAcct
		self._PrtctSfkpgAcct = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctSfkpgAcct', type=RestrictedFINMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=RestrictedFINMax15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ProtectTransactionType2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

