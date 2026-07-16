# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CardPaymentEnvironment82
from . import ResponseType10
from . import TransactionReconciliation5

class AcceptorReconciliationResponse12(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_Tx", "_TxRspn"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if value is not None else base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = base_types.UninitialisedField(self, 'Envt', CardPaymentEnvironment82, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', TransactionReconciliation5, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', TransactionReconciliation5, False)

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if value is not None else base_types.UninitialisedField(self, 'TxRspn', ResponseType10, False)

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = base_types.UninitialisedField(self, 'TxRspn', ResponseType10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=TransactionReconciliation5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType10, min=1, max=1, mutex_group=None, array=False),
	))