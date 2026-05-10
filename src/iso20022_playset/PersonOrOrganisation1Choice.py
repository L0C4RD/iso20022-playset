import base_types
import InternalPartyRole1Code
import PersonIdentification10
import LEIIdentifier
import MICIdentifier

class PersonOrOrganisation1Choice(base_types._BaseFieldType):

	__slots__ = ["_Prsn", "_Intl", "_MIC", "_LEI"]
	@property
	def Prsn(self):
		return self._Prsn

	@Prsn.setter
	def Prsn(self, value):
		self._Prsn = value if type(value) != auto else self.make_default("Prsn")

	@Prsn.deleter
	def Prsn(self):
		del self._Prsn
		self._Prsn = None

	@property
	def Intl(self):
		return self._Intl

	@Intl.setter
	def Intl(self, value):
		self._Intl = value if type(value) != auto else self.make_default("Intl")

	@Intl.deleter
	def Intl(self):
		del self._Intl
		self._Intl = None

	@property
	def MIC(self):
		return self._MIC

	@MIC.setter
	def MIC(self, value):
		self._MIC = value if type(value) != auto else self.make_default("MIC")

	@MIC.deleter
	def MIC(self):
		del self._MIC
		self._MIC = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prsn', type=PersonIdentification10, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Intl', type=InternalPartyRole1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MIC', type=MICIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
	))

