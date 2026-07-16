# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMContext13
from . import ATMTransaction45
from . import AutomatedTellerMachine3

class ATMCompletionAcknowledgement3(base_types._BaseFieldType):

	__slots__ = ["_ATM", "_Cntxt", "_Tx"]
	@property
	def ATM(self):
		return self._ATM

	@ATM.setter
	def ATM(self, value):
		self._ATM = value if value is not None else base_types.UninitialisedField(self, 'ATM', AutomatedTellerMachine3, False)

	@ATM.deleter
	def ATM(self):
		del self._ATM
		self._ATM = base_types.UninitialisedField(self, 'ATM', AutomatedTellerMachine3, False)

	@property
	def Cntxt(self):
		return self._Cntxt

	@Cntxt.setter
	def Cntxt(self, value):
		self._Cntxt = value if value is not None else base_types.UninitialisedField(self, 'Cntxt', ATMContext13, False)

	@Cntxt.deleter
	def Cntxt(self):
		del self._Cntxt
		self._Cntxt = base_types.UninitialisedField(self, 'Cntxt', ATMContext13, False)

	@property
	def Tx(self):
		return self._Tx

	@Tx.setter
	def Tx(self, value):
		self._Tx = value if value is not None else base_types.UninitialisedField(self, 'Tx', ATMTransaction45, False)

	@Tx.deleter
	def Tx(self):
		del self._Tx
		self._Tx = base_types.UninitialisedField(self, 'Tx', ATMTransaction45, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntxt', type=ATMContext13, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tx', type=ATMTransaction45, min=1, max=1, mutex_group=None, array=False),
	))