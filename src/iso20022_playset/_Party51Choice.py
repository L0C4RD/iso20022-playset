# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._PartyIdentification272 import PartyIdentification272

class Party51Choice(base_types._BaseFieldType):

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
		base_types.FieldEntry(name='FIId', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgId', type=PartyIdentification272, min=0, max=1, mutex_group=1, array=False),
	))