# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Acquirer7 import Acquirer7
from ._Acquirer8 import Acquirer8
from ._AutomatedTellerMachine3 import AutomatedTellerMachine3
from ._TerminalHosting1 import TerminalHosting1

class ATMEnvironment7(base_types._BaseFieldType):

	__slots__ = ["_ATM", "_ATMMgr", "_Acqrr", "_HstgNtty"]
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
	def ATMMgr(self):
		return self._ATMMgr

	@ATMMgr.setter
	def ATMMgr(self, value):
		self._ATMMgr = value if type(value) != base_types.auto else self.make_default("ATMMgr")

	@ATMMgr.deleter
	def ATMMgr(self):
		del self._ATMMgr
		self._ATMMgr = None

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
	def HstgNtty(self):
		return self._HstgNtty

	@HstgNtty.setter
	def HstgNtty(self, value):
		self._HstgNtty = value if type(value) != base_types.auto else self.make_default("HstgNtty")

	@HstgNtty.deleter
	def HstgNtty(self):
		del self._HstgNtty
		self._HstgNtty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMMgr', type=Acquirer8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstgNtty', type=TerminalHosting1, min=0, max=1, mutex_group=None, array=False),
	))