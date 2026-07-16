# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExternalAgentInstruction1Code
from . import Max140Text

class InstructionForAssignee1(base_types._BaseFieldType):

	__slots__ = ["_Cd", "_InstrInf"]
	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if value is not None else base_types.UninitialisedField(self, 'Cd', ExternalAgentInstruction1Code, False)

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = base_types.UninitialisedField(self, 'Cd', ExternalAgentInstruction1Code, False)

	@property
	def InstrInf(self):
		return self._InstrInf

	@InstrInf.setter
	def InstrInf(self, value):
		self._InstrInf = value if value is not None else base_types.UninitialisedField(self, 'InstrInf', Max140Text, False)

	@InstrInf.deleter
	def InstrInf(self):
		del self._InstrInf
		self._InstrInf = base_types.UninitialisedField(self, 'InstrInf', Max140Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cd', type=ExternalAgentInstruction1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))