from . import base_types
from ._CardPaymentEnvironment81 import CardPaymentEnvironment81
from ._CardPaymentTransaction143 import CardPaymentTransaction143
from ._Max9NumericText import Max9NumericText
from ._PaymentContext30 import PaymentContext30
from ._Traceability8 import Traceability8

class CardPaymentDataSetTransaction50(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_Envt", "_Tracblt", "_Tx", "_TxSeqCntr"]
	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if type(value) != base_types.auto else self.make_default("Cntxt")

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = None

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
	def Tracblt(self):
		return self._Tracblt

	@Tracblt.setter
	def Tracblt(self, value):
		self._Tracblt = value if type(value) != base_types.auto else self.make_default("Tracblt")

	@Tracblt.deleter
	def Tracblt(self):
		del self._Tracblt
		self._Tracblt = None

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
		base_types.FieldEntry(name='Cntxt', type=PaymentContext30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tracblt', type=Traceability8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransaction143, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSeqCntr', type=Max9NumericText, min=1, max=1, mutex_group=None, array=False),
	))

