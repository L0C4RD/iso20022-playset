from . import base_types
from ._CountryCode import CountryCode
from ._GenericIdentification5 import GenericIdentification5
from ._SafekeepingPlaceAsCodeAndPartyIdentification import SafekeepingPlaceAsCodeAndPartyIdentification

class SafekeepingPlaceFormatChoice(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdAsCtry", "_IdAsDSS"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def IdAsCtry(self):
		return self._IdAsCtry

	@IdAsCtry.setter
	def IdAsCtry(self, value):
		self._IdAsCtry = value if type(value) != base_types.auto else self.make_default("IdAsCtry")

	@IdAsCtry.deleter
	def IdAsCtry(self):
		del self._IdAsCtry
		self._IdAsCtry = None

	@property
	def IdAsDSS(self):
		return self._IdAsDSS

	@IdAsDSS.setter
	def IdAsDSS(self, value):
		self._IdAsDSS = value if type(value) != base_types.auto else self.make_default("IdAsDSS")

	@IdAsDSS.deleter
	def IdAsDSS(self):
		del self._IdAsDSS
		self._IdAsDSS = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=SafekeepingPlaceAsCodeAndPartyIdentification, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdAsCtry', type=CountryCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IdAsDSS', type=GenericIdentification5, min=0, max=1, mutex_group=1, array=False),
	))

