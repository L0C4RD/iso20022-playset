from . import base_types
from .Max35Text import Max35Text
from .PaymentCard36 import PaymentCard36
from .TerminalHosting1 import TerminalHosting1
from .ATMCustomer8 import ATMCustomer8
from .AutomatedTellerMachine12 import AutomatedTellerMachine12
from .Acquirer7 import Acquirer7

class ATMEnvironment18(base_types._BaseFieldType):

	__slots__ = ["_ATM", "_HstgNtty", "_Card", "_Cstmr", "_Acqrr", "_ATMMgrId"]
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
	def HstgNtty(self):
		return self._HstgNtty

	@HstgNtty.setter
	def HstgNtty(self, value):
		self._HstgNtty = value if type(value) != base_types.auto else self.make_default("HstgNtty")

	@HstgNtty.deleter
	def HstgNtty(self):
		del self._HstgNtty
		self._HstgNtty = None

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != base_types.auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

	@property
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if type(value) != base_types.auto else self.make_default("Cstmr")

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = None

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if type(value) != base_types.auto else self.make_default("Acqrr")

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = None

	@property
	def ATMMgrId(self):
		return self._ATMMgrId

	@ATMMgrId.setter
	def ATMMgrId(self, value):
		self._ATMMgrId = value if type(value) != base_types.auto else self.make_default("ATMMgrId")

	@ATMMgrId.deleter
	def ATMMgrId(self):
		del self._ATMMgrId
		self._ATMMgrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine12, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstgNtty', type=TerminalHosting1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cstmr', type=ATMCustomer8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMMgrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

