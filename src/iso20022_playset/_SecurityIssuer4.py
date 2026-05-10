from . import base_types
from .OrganisationIdentification15Choice import OrganisationIdentification15Choice
from .CountryCode import CountryCode

class SecurityIssuer4(base_types._BaseFieldType):

	__slots__ = ["_JursdctnCtry", "_Id"]
	@property
	def JursdctnCtry(self):
		return self._JursdctnCtry

	@JursdctnCtry.setter
	def JursdctnCtry(self, value):
		self._JursdctnCtry = value if type(value) != base_types.auto else self.make_default("JursdctnCtry")

	@JursdctnCtry.deleter
	def JursdctnCtry(self):
		del self._JursdctnCtry
		self._JursdctnCtry = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='JursdctnCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
	))

