import base_types
import Max35Text
import Acquirer7
import PaymentCard37
import AutomatedTellerMachine8
import TerminalHosting1

class ATMEnvironment22(base_types._BaseFieldType):

	__slots__ = ["_ATMMgrId", "_Card", "_ATM", "_HstgNtty", "_Acqrr"]
	@property
	def ATMMgrId(self):
		return self._ATMMgrId

	@ATMMgrId.setter
	def ATMMgrId(self, value):
		self._ATMMgrId = value if type(value) != auto else self.make_default("ATMMgrId")

	@ATMMgrId.deleter
	def ATMMgrId(self):
		del self._ATMMgrId
		self._ATMMgrId = None

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if type(value) != auto else self.make_default("Card")

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = None

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

	@property
	def HstgNtty(self):
		return self._HstgNtty

	@HstgNtty.setter
	def HstgNtty(self, value):
		self._HstgNtty = value if type(value) != auto else self.make_default("HstgNtty")

	@HstgNtty.deleter
	def HstgNtty(self):
		del self._HstgNtty
		self._HstgNtty = None

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if type(value) != auto else self.make_default("Acqrr")

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATMMgrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstgNtty', type=TerminalHosting1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
	))

