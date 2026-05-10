from . import base_types
from ._PaymentCommon6 import PaymentCommon6
from ._TransactionReport8 import TransactionReport8
from ._NumberAndSumOfTransactions2 import NumberAndSumOfTransactions2

class Transactions11(base_types._BaseFieldType):

	__slots__ = ["_TxsSummry", "_PmtCmonInf", "_TxRpt"]
	@property
	def PmtCmonInf(self):
		return self._PmtCmonInf

	@PmtCmonInf.setter
	def PmtCmonInf(self, value):
		self._PmtCmonInf = value if type(value) != base_types.auto else self.make_default("PmtCmonInf")

	@PmtCmonInf.deleter
	def PmtCmonInf(self):
		del self._PmtCmonInf
		self._PmtCmonInf = None

	@property
	def TxRpt(self):
		return self._TxRpt

	@TxRpt.setter
	def TxRpt(self, value):
		self._TxRpt = value if type(value) != base_types.auto else self.make_default("TxRpt")

	@TxRpt.deleter
	def TxRpt(self):
		del self._TxRpt
		self._TxRpt = None

	@property
	def TxsSummry(self):
		return self._TxsSummry

	@TxsSummry.setter
	def TxsSummry(self, value):
		self._TxsSummry = value if type(value) != base_types.auto else self.make_default("TxsSummry")

	@TxsSummry.deleter
	def TxsSummry(self):
		del self._TxsSummry
		self._TxsSummry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtCmonInf', type=PaymentCommon6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRpt', type=TransactionReport8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxsSummry', type=NumberAndSumOfTransactions2, min=0, max=1, mutex_group=None, array=False),
	))

