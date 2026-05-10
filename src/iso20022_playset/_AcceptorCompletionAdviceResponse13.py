from . import base_types
from ._CardPaymentEnvironment81 import CardPaymentEnvironment81
from ._CardPaymentTransactionAdviceResponse8 import CardPaymentTransactionAdviceResponse8
from ._SupplementaryData1 import SupplementaryData1
from ._TMSTrigger1 import TMSTrigger1

class AcceptorCompletionAdviceResponse13(base_types._BaseFieldType):

	__slots__ = ["_Envt", "_SplmtryData", "_TMSTrggr", "_Tx"]
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
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TMSTrggr(self):
		return self._TMSTrggr

	@TMSTrggr.setter
	def TMSTrggr(self, value):
		self._TMSTrggr = value if type(value) != base_types.auto else self.make_default("TMSTrggr")

	@TMSTrggr.deleter
	def TMSTrggr(self):
		del self._TMSTrggr
		self._TMSTrggr = None

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
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMSTrggr', type=TMSTrigger1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=CardPaymentTransactionAdviceResponse8, min=1, max=1, mutex_group=None, array=False),
	))

