# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentDataSet39 import CardPaymentDataSet39
from ._TransactionTotals12 import TransactionTotals12

class CardPaymentBatchTransferResponse12(base_types._BaseFieldType):

	__slots__ = ["_DataSet", "_TxTtls"]
	@property
	def DataSet(self):
		return self._DataSet

	@DataSet.setter
	def DataSet(self, value):
		self._DataSet = value if type(value) != base_types.auto else self.make_default("DataSet")

	@DataSet.deleter
	def DataSet(self):
		del self._DataSet
		self._DataSet = None

	@property
	def TxTtls(self):
		return self._TxTtls

	@TxTtls.setter
	def TxTtls(self, value):
		self._TxTtls = value if type(value) != base_types.auto else self.make_default("TxTtls")

	@TxTtls.deleter
	def TxTtls(self):
		del self._TxTtls
		self._TxTtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DataSet', type=CardPaymentDataSet39, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxTtls', type=TransactionTotals12, min=0, max=None, mutex_group=None, array=True),
	))