from . import base_types
from ._CardPaymentEnvironment82 import CardPaymentEnvironment82
from ._CardPaymentTransaction117 import CardPaymentTransaction117
from ._CardPaymentTransaction153 import CardPaymentTransaction153

class AcceptorCancellationResponse14(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_Tx", "_TxRspn"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment82, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction117, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=CardPaymentTransaction153, min=1, max=1, mutex_group=None, array=False),
	))

