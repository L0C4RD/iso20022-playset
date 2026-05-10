from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._PartyIdentification272 import PartyIdentification272

class Party50Choice(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pty', type=PartyIdentification272, min=0, max=1, mutex_group=1, array=False),
	))

