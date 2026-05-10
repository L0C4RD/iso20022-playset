from . import base_types
from ._BranchAndFinancialInstitutionIdentification6 import BranchAndFinancialInstitutionIdentification6
from ._PartyIdentification135 import PartyIdentification135

class Party44Choice(base_types._BaseFieldType):

	__slots__ = ["_FIId", "_OrgId"]
	@property
	def FIId(self):
		return self._FIId

	@FIId.setter
	def FIId(self, value):
		self._FIId = value if type(value) != base_types.auto else self.make_default("FIId")

	@FIId.deleter
	def FIId(self):
		del self._FIId
		self._FIId = None

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
		base_types.FieldEntry(name='FIId', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgId', type=PartyIdentification135, min=0, max=1, mutex_group=1, array=False),
	))

