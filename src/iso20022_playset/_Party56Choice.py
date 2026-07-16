# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstitutionIdentification19
from . import OrganisationIdentification39

class Party56Choice(base_types._BaseFieldType):

	__slots__ = ["_FIId", "_OrgId"]
	@property
	def FIId(self):
		return self._FIId

	@FIId.setter
	def FIId(self, value):
		self._FIId = value if value is not None else base_types.UninitialisedField(self, 'FIId', FinancialInstitutionIdentification19, False)

	@FIId.deleter
	def FIId(self):
		del self._FIId
		self._FIId = base_types.UninitialisedField(self, 'FIId', FinancialInstitutionIdentification19, False)

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if value is not None else base_types.UninitialisedField(self, 'OrgId', OrganisationIdentification39, False)

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = base_types.UninitialisedField(self, 'OrgId', OrganisationIdentification39, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FIId', type=FinancialInstitutionIdentification19, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=0, max=1, mutex_group=1, array=False),
	))