# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Acquirer7
from . import Acquirer8
from . import AutomatedTellerMachine3
from . import TerminalHosting1

class ATMEnvironment7(base_types._BaseFieldType):

	__slots__ = ["_ATM", "_ATMMgr", "_Acqrr", "_HstgNtty"]
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
	def ATMMgr(self):
		return self._ATMMgr

	@ATMMgr.setter
	def ATMMgr(self, value):
		self._ATMMgr = value if value is not None else base_types.UninitialisedField(self, 'ATMMgr', Acquirer8, False)

	@ATMMgr.deleter
	def ATMMgr(self):
		del self._ATMMgr
		self._ATMMgr = base_types.UninitialisedField(self, 'ATMMgr', Acquirer8, False)

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
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMMgr', type=Acquirer8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstgNtty', type=TerminalHosting1, min=0, max=1, mutex_group=None, array=False),
	))