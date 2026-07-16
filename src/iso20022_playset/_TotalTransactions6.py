# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NumberAndSumOfTransactions1
from . import NumberAndSumOfTransactions4
from . import TotalsPerBankTransactionCode5

class TotalTransactions6(base_types._BaseFieldType):

	__slots__ = ["_TtlCdtNtries", "_TtlDbtNtries", "_TtlNtries", "_TtlNtriesPerBkTxCd"]
	@property
	def TtlCdtNtries(self):
		return self._TtlCdtNtries

	@TtlCdtNtries.setter
	def TtlCdtNtries(self, value):
		self._TtlCdtNtries = value if value is not None else base_types.UninitialisedField(self, 'TtlCdtNtries', NumberAndSumOfTransactions1, False)

	@TtlCdtNtries.deleter
	def TtlCdtNtries(self):
		del self._TtlCdtNtries
		self._TtlCdtNtries = base_types.UninitialisedField(self, 'TtlCdtNtries', NumberAndSumOfTransactions1, False)

	@property
	def TtlDbtNtries(self):
		return self._TtlDbtNtries

	@TtlDbtNtries.setter
	def TtlDbtNtries(self, value):
		self._TtlDbtNtries = value if value is not None else base_types.UninitialisedField(self, 'TtlDbtNtries', NumberAndSumOfTransactions1, False)

	@TtlDbtNtries.deleter
	def TtlDbtNtries(self):
		del self._TtlDbtNtries
		self._TtlDbtNtries = base_types.UninitialisedField(self, 'TtlDbtNtries', NumberAndSumOfTransactions1, False)

	@property
	def TtlNtries(self):
		return self._TtlNtries

	@TtlNtries.setter
	def TtlNtries(self, value):
		self._TtlNtries = value if value is not None else base_types.UninitialisedField(self, 'TtlNtries', NumberAndSumOfTransactions4, False)

	@TtlNtries.deleter
	def TtlNtries(self):
		del self._TtlNtries
		self._TtlNtries = base_types.UninitialisedField(self, 'TtlNtries', NumberAndSumOfTransactions4, False)

	@property
	def TtlNtriesPerBkTxCd(self):
		return self._TtlNtriesPerBkTxCd

	@TtlNtriesPerBkTxCd.setter
	def TtlNtriesPerBkTxCd(self, value):
		self._TtlNtriesPerBkTxCd = value if value is not None else base_types.UninitialisedField(self, 'TtlNtriesPerBkTxCd', TotalsPerBankTransactionCode5, True)

	@TtlNtriesPerBkTxCd.deleter
	def TtlNtriesPerBkTxCd(self):
		del self._TtlNtriesPerBkTxCd
		self._TtlNtriesPerBkTxCd = base_types.UninitialisedField(self, 'TtlNtriesPerBkTxCd', TotalsPerBankTransactionCode5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlCdtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlDbtNtries', type=NumberAndSumOfTransactions1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNtries', type=NumberAndSumOfTransactions4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNtriesPerBkTxCd', type=TotalsPerBankTransactionCode5, min=0, max=None, mutex_group=None, array=True),
	))