import base_types
import GenericOrganisationIdentification1
import AnyBICIdentifier

class OrganisationIdentification4(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_BICOrBEI"]
	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def BICOrBEI(self):
		return self._BICOrBEI

	@BICOrBEI.setter
	def BICOrBEI(self, value):
		self._BICOrBEI = value if type(value) != auto else self.make_default("BICOrBEI")

	@BICOrBEI.deleter
	def BICOrBEI(self):
		del self._BICOrBEI
		self._BICOrBEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Othr', type=GenericOrganisationIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BICOrBEI', type=AnyBICIdentifier, min=0, max=1, mutex_group=None, array=False),
	))

