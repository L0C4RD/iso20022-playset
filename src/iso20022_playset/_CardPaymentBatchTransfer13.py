# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentDataSet40
from . import TransactionTotals12

class CardPaymentBatchTransfer13(base_types._BaseFieldType):

	__slots__ = ["_DataSet", "_TxTtls"]
	@property
	def DataSet(self):
		return self._DataSet

	@DataSet.setter
	def DataSet(self, value):
		self._DataSet = value if value is not None else base_types.UninitialisedField(self, 'DataSet', CardPaymentDataSet40, True)

	@DataSet.deleter
	def DataSet(self):
		del self._DataSet
		self._DataSet = base_types.UninitialisedField(self, 'DataSet', CardPaymentDataSet40, True)

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if value is not None else base_types.UninitialisedField(self, 'TxTtls', TransactionTotals12, True)

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = base_types.UninitialisedField(self, 'TxTtls', TransactionTotals12, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSet', type=CardPaymentDataSet40, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=0, max=None, mutex_group=None, array=True),
	))