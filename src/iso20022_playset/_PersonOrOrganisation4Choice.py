from . import base_types
from .PartyExceptionType1Code import PartyExceptionType1Code
from .GenericPersonIdentification1 import GenericPersonIdentification1
from .LEIIdentifier import LEIIdentifier

class PersonOrOrganisation4Choice(base_types._BaseFieldType):

	__slots__ = ["_LEI", "_XcptnId", "_Prsn"]
	@property
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	@property
	def XcptnId(self):
		return self._XcptnId

	@XcptnId.setter
	def XcptnId(self, value):
		self._XcptnId = value if type(value) != base_types.auto else self.make_default("XcptnId")

	@XcptnId.deleter
	def XcptnId(self):
		del self._XcptnId
		self._XcptnId = None

	@property
	def Prsn(self):
		return self._Prsn

	@Prsn.setter
	def Prsn(self, value):
		self._Prsn = value if type(value) != base_types.auto else self.make_default("Prsn")

	@Prsn.deleter
	def Prsn(self):
		del self._Prsn
		self._Prsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='XcptnId', type=PartyExceptionType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Prsn', type=GenericPersonIdentification1, min=0, max=1, mutex_group=1, array=False),
	))

