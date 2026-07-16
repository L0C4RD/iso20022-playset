# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCustomer9
from . import Acquirer7
from . import Acquirer8
from . import AutomatedTellerMachine2
from . import ContentInformationType10
from . import PlainCardData24
from . import TerminalHosting1

class ATMEnvironment21(base_types._BaseFieldType):

	__slots__ = ["_ATM", "_ATMMgr", "_Acqrr", "_Cstmr", "_HstgNtty", "_PlainCardData", "_PrtctdCardData"]
	@property
	def ATM(self):
		return self._ATM

	@ATM.setter
	def ATM(self, value):
		self._ATM = value if value is not None else base_types.UninitialisedField(self, 'ATM', AutomatedTellerMachine2, False)

	@ATM.deleter
	def ATM(self):
		del self._ATM
		self._ATM = base_types.UninitialisedField(self, 'ATM', AutomatedTellerMachine2, False)

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
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if value is not None else base_types.UninitialisedField(self, 'Cstmr', ATMCustomer9, False)

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = base_types.UninitialisedField(self, 'Cstmr', ATMCustomer9, False)

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

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if value is not None else base_types.UninitialisedField(self, 'PlainCardData', PlainCardData24, False)

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = base_types.UninitialisedField(self, 'PlainCardData', PlainCardData24, False)

	@property
	def PrtctdCardData(self):
		return self._PrtctdCardData

	@PrtctdCardData.setter
	def PrtctdCardData(self, value):
		self._PrtctdCardData = value if value is not None else base_types.UninitialisedField(self, 'PrtctdCardData', ContentInformationType10, False)

	@PrtctdCardData.deleter
	def PrtctdCardData(self):
		del self._PrtctdCardData
		self._PrtctdCardData = base_types.UninitialisedField(self, 'PrtctdCardData', ContentInformationType10, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMMgr', type=Acquirer8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cstmr', type=ATMCustomer9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstgNtty', type=TerminalHosting1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlainCardData', type=PlainCardData24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCardData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
	))