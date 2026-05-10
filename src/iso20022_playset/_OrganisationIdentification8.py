from . import base_types
from ._AnyBICIdentifier import AnyBICIdentifier
from ._GenericOrganisationIdentification1 import GenericOrganisationIdentification1

class OrganisationIdentification8(base_types._BaseFieldType):

	__slots__ = ["_AnyBIC", "_Othr"]
	@property
	def AnyBIC(self):
		return self._AnyBIC

	@AnyBIC.setter
	def AnyBIC(self, value):
		self._AnyBIC = value if type(value) != base_types.auto else self.make_default("AnyBIC")

	@AnyBIC.deleter
	def AnyBIC(self):
		del self._AnyBIC
		self._AnyBIC = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyBIC', type=AnyBICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericOrganisationIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

