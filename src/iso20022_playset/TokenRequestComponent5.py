from . import base_types
from .Max9NumericText import Max9NumericText
from .CardPaymentEnvironment81 import CardPaymentEnvironment81

class TokenRequestComponent5(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_TxSeqCntr"]
	@property
	def Envt(self):
		return self._Envt

	@Envt.setter
	def Envt(self, value):
		self._Envt = value if type(value) != auto else self.make_default("Envt")

	@Envt.deleter
	def Envt(self):
		del self._Envt
		self._Envt = None

	@property
	def TxSeqCntr(self):
		return self._TxSeqCntr

	@TxSeqCntr.setter
	def TxSeqCntr(self, value):
		self._TxSeqCntr = value if type(value) != auto else self.make_default("TxSeqCntr")

	@TxSeqCntr.deleter
	def TxSeqCntr(self):
		del self._TxSeqCntr
		self._TxSeqCntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Envt', type=CardPaymentEnvironment81, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSeqCntr', type=Max9NumericText, min=1, max=1, mutex_group=None, array=False),
	))

