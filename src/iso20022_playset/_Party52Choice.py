from . import base_types
from ._OrganisationIdentification39 import OrganisationIdentification39
from ._PersonIdentification18 import PersonIdentification18

class Party52Choice(base_types._BaseFieldType):

	__slots__ = ["_PrvtId", "_OrgId"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrvtId', type=PersonIdentification18, min=0, max=1, mutex_group=1, array=False),
	))

