from . import base_types
from ._PersonIdentification3 import PersonIdentification3
from ._OrganisationIdentification2 import OrganisationIdentification2

class Party2Choice(base_types._BaseFieldType):

	__slots__ = ["_PrvtId", "_OrgId"]
	@property
	def PrvtId(self):
		return self._PrvtId

	@PrvtId.setter
	def PrvtId(self, value):
		self._PrvtId = value if type(value) != base_types.auto else self.make_default("PrvtId")

	@PrvtId.deleter
	def PrvtId(self):
		del self._PrvtId
		self._PrvtId = None

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if type(value) != base_types.auto else self.make_default("OrgId")

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvtId', type=PersonIdentification3, min=1, max=4, mutex_group=1, array=True),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification2, min=0, max=1, mutex_group=1, array=False),
	))

