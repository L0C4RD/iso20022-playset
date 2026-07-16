# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import OrganisationIdentification39

class Organisation44(base_types._BaseFieldType):

	__slots__ = ["_FullLglNm", "_OrgId"]
	@property
	def FullLglNm(self):
		return self._FullLglNm

	@FullLglNm.setter
	def FullLglNm(self, value):
		self._FullLglNm = value if value is not None else base_types.UninitialisedField(self, 'FullLglNm', Max350Text, False)

	@FullLglNm.deleter
	def FullLglNm(self):
		del self._FullLglNm
		self._FullLglNm = base_types.UninitialisedField(self, 'FullLglNm', Max350Text, False)

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
		base_types.FieldEntry(name='FullLglNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgId', type=OrganisationIdentification39, min=1, max=1, mutex_group=None, array=False),
	))