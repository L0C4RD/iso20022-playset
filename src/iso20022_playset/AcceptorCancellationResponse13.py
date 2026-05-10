from . import base_types
from .CardPaymentEnvironment81 import CardPaymentEnvironment81
from .CardPaymentTransaction145 import CardPaymentTransaction145
from .CardPaymentTransaction117 import CardPaymentTransaction117

class AcceptorCancellationResponse13(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_TxRspn", "_Tx"]
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
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != base_types.auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=CardPaymentTransaction145, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction117, min=1, max=1, mutex_group=None, array=False),
	))

