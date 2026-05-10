from . import base_types
from .TerminalHosting1 import TerminalHosting1
from .Acquirer7 import Acquirer7
from .ContentInformationType10 import ContentInformationType10
from .AutomatedTellerMachine2 import AutomatedTellerMachine2
from .Acquirer8 import Acquirer8
from .PlainCardData24 import PlainCardData24
from .ATMCustomer9 import ATMCustomer9

class ATMEnvironment21(base_types._BaseFieldType):

	__slots__ = ["_Cstmr", "_PlainCardData", "_ATMMgr", "_ATM", "_HstgNtty", "_PrtctdCardData", "_Acqrr"]
	@property
	def Cstmr(self):
		return self._Cstmr

	@Cstmr.setter
	def Cstmr(self, value):
		self._Cstmr = value if type(value) != auto else self.make_default("Cstmr")

	@Cstmr.deleter
	def Cstmr(self):
		del self._Cstmr
		self._Cstmr = None

	@property
	def PlainCardData(self):
		return self._PlainCardData

	@PlainCardData.setter
	def PlainCardData(self, value):
		self._PlainCardData = value if type(value) != auto else self.make_default("PlainCardData")

	@PlainCardData.deleter
	def PlainCardData(self):
		del self._PlainCardData
		self._PlainCardData = None

	@property
	def ATMMgr(self):
		return self._ATMMgr

	@ATMMgr.setter
	def ATMMgr(self, value):
		self._ATMMgr = value if type(value) != auto else self.make_default("ATMMgr")

	@ATMMgr.deleter
	def ATMMgr(self):
		del self._ATMMgr
		self._ATMMgr = None

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
	def PrtctdCardData(self):
		return self._PrtctdCardData

	@PrtctdCardData.setter
	def PrtctdCardData(self, value):
		self._PrtctdCardData = value if type(value) != auto else self.make_default("PrtctdCardData")

	@PrtctdCardData.deleter
	def PrtctdCardData(self):
		del self._PrtctdCardData
		self._PrtctdCardData = None

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
		base_types.FieldEntry(name='Cstmr', type=ATMCustomer9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PlainCardData', type=PlainCardData24, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMMgr', type=Acquirer8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstgNtty', type=TerminalHosting1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtctdCardData', type=ContentInformationType10, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
	))

