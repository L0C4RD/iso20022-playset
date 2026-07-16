# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CountryCode
from . import OrganisationIdentification15Choice

class SecurityIssuer4(base_types._BaseFieldType):

	__slots__ = ["_Id", "_JursdctnCtry"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', OrganisationIdentification15Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', OrganisationIdentification15Choice, False)

	@property
	def JursdctnCtry(self):
		return self._JursdctnCtry

	@JursdctnCtry.setter
	def JursdctnCtry(self, value):
		self._JursdctnCtry = value if value is not None else base_types.UninitialisedField(self, 'JursdctnCtry', CountryCode, False)

	@JursdctnCtry.deleter
	def JursdctnCtry(self):
		del self._JursdctnCtry
		self._JursdctnCtry = base_types.UninitialisedField(self, 'JursdctnCtry', CountryCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='JursdctnCtry', type=CountryCode, min=1, max=1, mutex_group=None, array=False),
	))