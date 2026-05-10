from . import base_types
import PartyIdentification272
import BranchAndFinancialInstitutionIdentification8

class Party50Choice(base_types._BaseFieldType):

	__slots__ = ["_Pty", "_Agt"]
	@property
	def Pty(self):
		return self._Pty

	@Pty.setter
	def Pty(self, value):
		self._Pty = value if type(value) != auto else self.make_default("Pty")

	@Pty.deleter
	def Pty(self):
		del self._Pty
		self._Pty = None

	@property
	def Agt(self):
		return self._Agt

	@Agt.setter
	def Agt(self, value):
		self._Agt = value if type(value) != auto else self.make_default("Agt")

	@Agt.deleter
	def Agt(self):
		del self._Agt
		self._Agt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pty', type=PartyIdentification272, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Agt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=1, array=False),
	))

