from . import base_types
from .CorporateAction1Choice import CorporateAction1Choice
from .TransactionType2Choice import TransactionType2Choice

class TransactionType1Choice(base_types._BaseFieldType):

	__slots__ = ["_TxTp", "_CorpActnTp"]
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
	def CorpActnTp(self):
		return self._CorpActnTp

	@CorpActnTp.setter
	def CorpActnTp(self, value):
		self._CorpActnTp = value if type(value) != auto else self.make_default("CorpActnTp")

	@CorpActnTp.deleter
	def CorpActnTp(self):
		del self._CorpActnTp
		self._CorpActnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxTp', type=TransactionType2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CorpActnTp', type=CorporateAction1Choice, min=0, max=1, mutex_group=1, array=False),
	))

