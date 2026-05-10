from . import base_types
import ATMTransaction52
import AutomatedTellerMachine3

class ATMReconciliationAcknowledgement3(base_types._BaseFieldType):

	__slots__ = ["_Tx", "_ATM"]
	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if type(value) != auto else self.make_default("Tx")

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = None

	@property
	def ATM(self):
		return self._ATM

	@ATM.setter
	def ATM(self, value):
		self._ATM = value if type(value) != auto else self.make_default("ATM")

	@ATM.deleter
	def ATM(self):
		del self._ATM
		self._ATM = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tx', type=ATMTransaction52, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine3, min=1, max=1, mutex_group=None, array=False),
	))

