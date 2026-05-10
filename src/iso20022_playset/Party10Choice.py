from . import base_types
import OrganisationIdentification7
import PersonIdentification5

class Party10Choice(base_types._BaseFieldType):

	__slots__ = ["_PrvtId", "_OrgId"]
	@property
	def PrvtId(self):
		return self._PrvtId

	@PrvtId.setter
	def PrvtId(self, value):
		self._PrvtId = value if type(value) != auto else self.make_default("PrvtId")

	@PrvtId.deleter
	def PrvtId(self):
		del self._PrvtId
		self._PrvtId = None

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if type(value) != auto else self.make_default("OrgId")

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrvtId', type=PersonIdentification5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification7, min=0, max=1, mutex_group=1, array=False),
	))

