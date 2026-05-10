from . import base_types
from .FinancialInstitutionIdentification10Choice import FinancialInstitutionIdentification10Choice
from .LEIIdentifier import LEIIdentifier

class FinancialInstitutionIdentification17(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_Pty"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pty', type=FinancialInstitutionIdentification10Choice, min=1, max=1, mutex_group=None, array=False),
	))

