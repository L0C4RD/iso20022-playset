from . import base_types
from .ATMTransaction45 import ATMTransaction45
from .ATMContext13 import ATMContext13
from .AutomatedTellerMachine3 import AutomatedTellerMachine3

class ATMCompletionAcknowledgement3(base_types._BaseFieldType):

	__slots__ = ["_Cntxt", "_ATM", "_Tx"]
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
	def ATM(self):
		return self._ATM

	@ATM.setter
	def ATM(self, value):
		self._ATM = value if type(value) != base_types.auto else self.make_default("ATM")

	@ATM.deleter
	def ATM(self):
		del self._ATM
		self._ATM = None

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
		base_types.FieldEntry(name='Cntxt', type=ATMContext13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=ATMTransaction45, min=1, max=1, mutex_group=None, array=False),
	))

