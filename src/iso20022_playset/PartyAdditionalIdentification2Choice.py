from . import base_types
from .OrganisationIdentification5 import OrganisationIdentification5
from .ISODate import ISODate

class PartyAdditionalIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_RegnId"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if type(value) != base_types.auto else self.make_default("BirthDt")

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = None

	@property
	def RegnId(self):
		return self._RegnId

	@RegnId.setter
	def RegnId(self, value):
		self._RegnId = value if type(value) != base_types.auto else self.make_default("RegnId")

	@RegnId.deleter
	def RegnId(self):
		del self._RegnId
		self._RegnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RegnId', type=OrganisationIdentification5, min=0, max=1, mutex_group=1, array=False),
	))

