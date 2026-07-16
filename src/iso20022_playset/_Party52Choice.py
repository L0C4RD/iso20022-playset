# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrganisationIdentification39
from . import PersonIdentification18

class Party52Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgId", "_PrvtId"]
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

	@property
	def PrvtId(self):
		return self._PrvtId

	@PrvtId.setter
	def PrvtId(self, value):
		self._PrvtId = value if value is not None else base_types.UninitialisedField(self, 'PrvtId', PersonIdentification18, False)

	@PrvtId.deleter
	def PrvtId(self):
		del self._PrvtId
		self._PrvtId = base_types.UninitialisedField(self, 'PrvtId', PersonIdentification18, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrvtId', type=PersonIdentification18, min=0, max=1, mutex_group=1, array=False),
	))