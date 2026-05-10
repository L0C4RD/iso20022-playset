import base_types
import BranchAndFinancialInstitutionIdentification5
import PartyIdentification42

class Party9Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgId", "_FIId"]
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

	@property
	def FIId(self):
		return self._FIId

	@FIId.setter
	def FIId(self, value):
		self._FIId = value if type(value) != auto else self.make_default("FIId")

	@FIId.deleter
	def FIId(self):
		del self._FIId
		self._FIId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgId', type=PartyIdentification42, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FIId', type=BranchAndFinancialInstitutionIdentification5, min=0, max=1, mutex_group=1, array=False),
	))

