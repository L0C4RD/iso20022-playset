import base_types
import QueryType2Code
import TransactionCriteria8Choice

class TransactionQuery8(base_types._BaseFieldType):

	__slots__ = ["_QryTp", "_TxCrit"]
	@property
	def QryTp(self):
		return self._QryTp

	@QryTp.setter
	def QryTp(self, value):
		self._QryTp = value if type(value) != auto else self.make_default("QryTp")

	@QryTp.deleter
	def QryTp(self):
		del self._QryTp
		self._QryTp = None

	@property
	def TxCrit(self):
		return self._TxCrit

	@TxCrit.setter
	def TxCrit(self, value):
		self._TxCrit = value if type(value) != auto else self.make_default("TxCrit")

	@TxCrit.deleter
	def TxCrit(self):
		del self._TxCrit
		self._TxCrit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QryTp', type=QueryType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxCrit', type=TransactionCriteria8Choice, min=0, max=1, mutex_group=None, array=False),
	))

