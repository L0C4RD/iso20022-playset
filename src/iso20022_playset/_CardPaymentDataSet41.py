# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CardPaymentEnvironment82 import CardPaymentEnvironment82
from ._CardPaymentTransactionAdviceResponse5 import CardPaymentTransactionAdviceResponse5
from ._Max9NumericText import Max9NumericText
from ._ResponseType10 import ResponseType10

class CardPaymentDataSet41(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_Tx", "_TxRspn", "_TxSeqCntr"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != base_types.auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if type(value) != base_types.auto else self.make_default("TxRspn")

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = None

	@property
	def TxSeqCntr(self):
		return self._TxSeqCntr

	@TxSeqCntr.setter
	def TxSeqCntr(self, value):
		self._TxSeqCntr = value if type(value) != base_types.auto else self.make_default("TxSeqCntr")

	@TxSeqCntr.deleter
	def TxSeqCntr(self):
		del self._TxSeqCntr
		self._TxSeqCntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransactionAdviceResponse5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType10, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSeqCntr', type=Max9NumericText, min=1, max=1, mutex_group=None, array=False),
	))