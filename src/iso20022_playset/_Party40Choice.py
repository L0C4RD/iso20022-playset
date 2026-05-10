from . import base_types
from .PartyIdentification135 import PartyIdentification135
from .BranchAndFinancialInstitutionIdentification6 import BranchAndFinancialInstitutionIdentification6

class Party40Choice(base_types._BaseFieldType):

	__slots__ = ["_Agt", "_Pty"]
	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != base_types.auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != base_types.auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification135, min=0, max=1, mutex_group=1, array=False),
	))

