from . import base_types
from .Max140Text import Max140Text
from .ExternalCreditorAgentInstruction1Code import ExternalCreditorAgentInstruction1Code

class InstructionForCreditorAgent3(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_InstrInf"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	@property
	def InstrInf(self):
		return self._InstrInf

	@InstrInf.setter
	def InstrInf(self, value):
		self._InstrInf = value if type(value) != base_types.auto else self.make_default("InstrInf")

	@InstrInf.deleter
	def InstrInf(self):
		del self._InstrInf
		self._InstrInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=ExternalCreditorAgentInstruction1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

