from . import base_types
from ._NumberAndSumOfTransactions1 import NumberAndSumOfTransactions1
from ._NumberAndSumOfTransactions4 import NumberAndSumOfTransactions4
from ._TotalsPerBankTransactionCode5 import TotalsPerBankTransactionCode5

class TotalTransactions6(base_types._BaseFieldType):

	__slots__ = ["_TtlCdtNtries", "_TtlDbtNtries", "_TtlNtries", "_TtlNtriesPerBkTxCd"]
	@property
	def TtlCdtNtries(self):
		return self._TtlCdtNtries

	@TtlCdtNtries.setter
	def TtlCdtNtries(self, value):
		self._TtlCdtNtries = value if type(value) != base_types.auto else self.make_default("TtlCdtNtries")

	@TtlCdtNtries.deleter
	def TtlCdtNtries(self):
		del self._TtlCdtNtries
		self._TtlCdtNtries = None

	@property
	def TtlDbtNtries(self):
		return self._TtlDbtNtries

	@TtlDbtNtries.setter
	def TtlDbtNtries(self, value):
		self._TtlDbtNtries = value if type(value) != base_types.auto else self.make_default("TtlDbtNtries")

	@TtlDbtNtries.deleter
	def TtlDbtNtries(self):
		del self._TtlDbtNtries
		self._TtlDbtNtries = None

	@property
	def TtlNtries(self):
		return self._TtlNtries

	@TtlNtries.setter
	def TtlNtries(self, value):
		self._TtlNtries = value if type(value) != base_types.auto else self.make_default("TtlNtries")

	@TtlNtries.deleter
	def TtlNtries(self):
		del self._TtlNtries
		self._TtlNtries = None

	@property
	def TtlNtriesPerBkTxCd(self):
		return self._TtlNtriesPerBkTxCd

	@TtlNtriesPerBkTxCd.setter
	def TtlNtriesPerBkTxCd(self, value):
		self._TtlNtriesPerBkTxCd = value if type(value) != base_types.auto else self.make_default("TtlNtriesPerBkTxCd")

	@TtlNtriesPerBkTxCd.deleter
	def TtlNtriesPerBkTxCd(self):
		del self._TtlNtriesPerBkTxCd
		self._TtlNtriesPerBkTxCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCdtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlDbtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNtries', type=NumberAndSumOfTransactions4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNtriesPerBkTxCd', type=TotalsPerBankTransactionCode5, min=0, max=None, mutex_group=None, array=True),
	))

