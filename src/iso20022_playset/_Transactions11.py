# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NumberAndSumOfTransactions2
from . import PaymentCommon6
from . import TransactionReport8

class Transactions11(base_types._BaseFieldType):

	__slots__ = ["_PmtCmonInf", "_TxRpt", "_TxsSummry"]
	@property
	def PmtCmonInf(self):
		return self._PmtCmonInf

	@PmtCmonInf.setter
	def PmtCmonInf(self, value):
		self._PmtCmonInf = value if value is not None else base_types.UninitialisedField(self, 'PmtCmonInf', PaymentCommon6, False)

	@PmtCmonInf.deleter
	def PmtCmonInf(self):
		del self._PmtCmonInf
		self._PmtCmonInf = base_types.UninitialisedField(self, 'PmtCmonInf', PaymentCommon6, False)

	@property
	def TxRpt(self):
		return self._TxRpt

	@TxRpt.setter
	def TxRpt(self, value):
		self._TxRpt = value if value is not None else base_types.UninitialisedField(self, 'TxRpt', TransactionReport8, True)

	@TxRpt.deleter
	def TxRpt(self):
		del self._TxRpt
		self._TxRpt = base_types.UninitialisedField(self, 'TxRpt', TransactionReport8, True)

	@property
	def TxsSummry(self):
		return self._TxsSummry

	@TxsSummry.setter
	def TxsSummry(self, value):
		self._TxsSummry = value if value is not None else base_types.UninitialisedField(self, 'TxsSummry', NumberAndSumOfTransactions2, False)

	@TxsSummry.deleter
	def TxsSummry(self):
		del self._TxsSummry
		self._TxsSummry = base_types.UninitialisedField(self, 'TxsSummry', NumberAndSumOfTransactions2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtCmonInf', type=PaymentCommon6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRpt', type=TransactionReport8, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxsSummry', type=NumberAndSumOfTransactions2, min=0, max=1, mutex_group=None, array=False),
	))