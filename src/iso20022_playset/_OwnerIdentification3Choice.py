from . import base_types
from .PartyIdentification139 import PartyIdentification139
from .IndividualPersonIdentification2Choice import IndividualPersonIdentification2Choice

class OwnerIdentification3Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgOwnrId", "_IndvOwnrId"]
	@property
	def OrgOwnrId(self):
		return self._OrgOwnrId

	@OrgOwnrId.setter
	def OrgOwnrId(self, value):
		self._OrgOwnrId = value if type(value) != base_types.auto else self.make_default("OrgOwnrId")

	@OrgOwnrId.deleter
	def OrgOwnrId(self):
		del self._OrgOwnrId
		self._OrgOwnrId = None

	@property
	def IndvOwnrId(self):
		return self._IndvOwnrId

	@IndvOwnrId.setter
	def IndvOwnrId(self, value):
		self._IndvOwnrId = value if type(value) != base_types.auto else self.make_default("IndvOwnrId")

	@IndvOwnrId.deleter
	def IndvOwnrId(self):
		del self._IndvOwnrId
		self._IndvOwnrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgOwnrId', type=PartyIdentification139, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IndvOwnrId', type=IndividualPersonIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
	))

