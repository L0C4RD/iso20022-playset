from . import base_types
from ._PaymentIdentification8Choice import PaymentIdentification8Choice
from ._TransactionOrError6Choice import TransactionOrError6Choice

class TransactionReport8(base_types._BaseFieldType):

	__slots__ = ["_PmtId", "_TxOrErr"]
	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if type(value) != base_types.auto else self.make_default("PmtId")

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = None

	@property
	def TxOrErr(self):
		return self._TxOrErr

	@TxOrErr.setter
	def TxOrErr(self, value):
		self._TxOrErr = value if type(value) != base_types.auto else self.make_default("TxOrErr")

	@TxOrErr.deleter
	def TxOrErr(self):
		del self._TxOrErr
		self._TxOrErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification8Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxOrErr', type=TransactionOrError6Choice, min=1, max=1, mutex_group=None, array=False),
	))

