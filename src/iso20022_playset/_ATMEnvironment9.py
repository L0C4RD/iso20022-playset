from . import base_types
from ._Acquirer7 import Acquirer7
from ._AutomatedTellerMachine7 import AutomatedTellerMachine7
from ._Max35Text import Max35Text

class ATMEnvironment9(base_types._BaseFieldType):

	__slots__ = ["_ATM", "_ATMMgrId", "_Acqrr"]
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
	def ATMMgrId(self):
		return self._ATMMgrId

	@ATMMgrId.setter
	def ATMMgrId(self, value):
		self._ATMMgrId = value if type(value) != base_types.auto else self.make_default("ATMMgrId")

	@ATMMgrId.deleter
	def ATMMgrId(self):
		del self._ATMMgrId
		self._ATMMgrId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ATM', type=AutomatedTellerMachine7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ATMMgrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Acqrr', type=Acquirer7, min=0, max=1, mutex_group=None, array=False),
	))

