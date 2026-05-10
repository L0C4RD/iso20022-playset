from . import base_types
from .GenericOrganisationIdentification1 import GenericOrganisationIdentification1
from .AnyBICIdentifier import AnyBICIdentifier

class OrganisationIdentification6(base_types._BaseFieldType):

	__slots__ = ["_BIC", "_Othr"]
	@property
	def BIC(self):
		return self._BIC

	@BIC.setter
	def BIC(self, value):
		self._BIC = value if type(value) != base_types.auto else self.make_default("BIC")

	@BIC.deleter
	def BIC(self):
		del self._BIC
		self._BIC = None

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
		base_types.FieldEntry(name='BIC', type=AnyBICIdentifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=GenericOrganisationIdentification1, min=0, max=None, mutex_group=None, array=True),
	))

