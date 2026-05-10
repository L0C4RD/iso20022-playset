from . import base_types
from .FinancialInstitutionIdentification21 import FinancialInstitutionIdentification21
from .PersonIdentification13 import PersonIdentification13
from .OrganisationIdentification29 import OrganisationIdentification29

class TrackerParty2Choice(base_types._BaseFieldType):

	__slots__ = ["_FinInstnId", "_OrgId", "_PrvtId"]
	@property
	def FinInstnId(self):
		return self._FinInstnId

	@FinInstnId.setter
	def FinInstnId(self, value):
		self._FinInstnId = value if type(value) != base_types.auto else self.make_default("FinInstnId")

	@FinInstnId.deleter
	def FinInstnId(self):
		del self._FinInstnId
		self._FinInstnId = None

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
		base_types.FieldEntry(name='FinInstnId', type=FinancialInstitutionIdentification21, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification29, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrvtId', type=PersonIdentification13, min=0, max=1, mutex_group=1, array=False),
	))

