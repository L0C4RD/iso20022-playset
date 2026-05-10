from . import base_types
from ._LegalPersonIdentification1 import LegalPersonIdentification1
from ._NaturalPersonIdentification3 import NaturalPersonIdentification3

class PartyIdentification248Choice(base_types._BaseFieldType):

	__slots__ = ["_Lgl", "_Ntrl"]
	@property
	def Lgl(self):
		return self._Lgl

	@Lgl.setter
	def Lgl(self, value):
		self._Lgl = value if type(value) != base_types.auto else self.make_default("Lgl")

	@Lgl.deleter
	def Lgl(self):
		del self._Lgl
		self._Lgl = None

	@property
	def Ntrl(self):
		return self._Ntrl

	@Ntrl.setter
	def Ntrl(self, value):
		self._Ntrl = value if type(value) != base_types.auto else self.make_default("Ntrl")

	@Ntrl.deleter
	def Ntrl(self):
		del self._Ntrl
		self._Ntrl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lgl', type=LegalPersonIdentification1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ntrl', type=NaturalPersonIdentification3, min=0, max=1, mutex_group=1, array=False),
	))

