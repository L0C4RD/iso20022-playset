# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification6
from . import PartyIdentification135

class Party44Choice(base_types._BaseFieldType):

	__slots__ = ["_FIId", "_OrgId"]
	@property
	def FIId(self):
		return self._FIId

	@FIId.setter
	def FIId(self, value):
		self._FIId = value if value is not None else base_types.UninitialisedField(self, 'FIId', BranchAndFinancialInstitutionIdentification6, False)

	@FIId.deleter
	def FIId(self):
		del self._FIId
		self._FIId = base_types.UninitialisedField(self, 'FIId', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def OrgId(self):
		return self._OrgId

	@OrgId.setter
	def OrgId(self, value):
		self._OrgId = value if value is not None else base_types.UninitialisedField(self, 'OrgId', PartyIdentification135, False)

	@OrgId.deleter
	def OrgId(self):
		del self._OrgId
		self._OrgId = base_types.UninitialisedField(self, 'OrgId', PartyIdentification135, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FIId', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgId', type=PartyIdentification135, min=0, max=1, mutex_group=1, array=False),
	))