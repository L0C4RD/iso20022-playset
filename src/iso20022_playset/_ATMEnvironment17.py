# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCustomer8
from . import Acquirer7
from . import AutomatedTellerMachine11
from . import Max35Text
from . import PaymentCard36
from . import TerminalHosting1

class ATMEnvironment17(base_types._BaseFieldType):

	__slots__ = ["_ATM", "_ATMMgrId", "_Acqrr", "_Card", "_Cstmr", "_HstgNtty"]
	@property
	def ATM(self):
		return self._ATM

	@ATM.setter
	def ATM(self, value):
		self._ATM = value if value is not None else base_types.UninitialisedField(self, 'ATM', AutomatedTellerMachine11, False)

	@ATM.deleter
	def ATM(self):
		del self._ATM
		self._ATM = base_types.UninitialisedField(self, 'ATM', AutomatedTellerMachine11, False)

	@property
	def ATMMgrId(self):
		return self._ATMMgrId

	@ATMMgrId.setter
	def ATMMgrId(self, value):
		self._ATMMgrId = value if value is not None else base_types.UninitialisedField(self, 'ATMMgrId', Max35Text, False)

	@ATMMgrId.deleter
	def ATMMgrId(self):
		del self._ATMMgrId
		self._ATMMgrId = base_types.UninitialisedField(self, 'ATMMgrId', Max35Text, False)

	@property
	def Acqrr(self):
		return self._Acqrr

	@Acqrr.setter
	def Acqrr(self, value):
		self._Acqrr = value if value is not None else base_types.UninitialisedField(self, 'Acqrr', Acquirer7, False)

	@Acqrr.deleter
	def Acqrr(self):
		del self._Acqrr
		self._Acqrr = base_types.UninitialisedField(self, 'Acqrr', Acquirer7, False)

	@property
	def Card(self):
		return self._Card

	@Card.setter
	def Card(self, value):
		self._Card = value if value is not None else base_types.UninitialisedField(self, 'Card', PaymentCard36, False)

	@Card.deleter
	def Card(self):
		del self._Card
		self._Card = base_types.UninitialisedField(self, 'Card', PaymentCard36, False)

	@property
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if value is not None else base_types.UninitialisedField(self, 'Cstmr', ATMCustomer8, False)

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = base_types.UninitialisedField(self, 'Cstmr', ATMCustomer8, False)

	@property
	def HstgNtty(self):
		return self._HstgNtty

	@HstgNtty.setter
	def HstgNtty(self, value):
		self._HstgNtty = value if value is not None else base_types.UninitialisedField(self, 'HstgNtty', TerminalHosting1, False)

	@HstgNtty.deleter
	def HstgNtty(self):
		del self._HstgNtty
		self._HstgNtty = base_types.UninitialisedField(self, 'HstgNtty', TerminalHosting1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMMgrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Card', type=PaymentCard36, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cstmr', type=ATMCustomer8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstgNtty', type=TerminalHosting1, min=0, max=1, mutex_group=None, array=False),
	))