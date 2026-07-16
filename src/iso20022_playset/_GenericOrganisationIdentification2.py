# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import OrganisationIdentificationSchemeName2Choice
from . import RestrictedFINXMax35Text

class GenericOrganisationIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Issr", "_SchmeNm"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', RestrictedFINXMax35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', RestrictedFINXMax35Text, False)

	@property
	def Issr(self):
		return self._Issr

	@Issr.setter
	def Issr(self, value):
		self._Issr = value if value is not None else base_types.UninitialisedField(self, 'Issr', RestrictedFINXMax35Text, False)

	@Issr.deleter
	def Issr(self):
		del self._Issr
		self._Issr = base_types.UninitialisedField(self, 'Issr', RestrictedFINXMax35Text, False)

	@property
	def SchmeNm(self):
		return self._SchmeNm

	@SchmeNm.setter
	def SchmeNm(self, value):
		self._SchmeNm = value if value is not None else base_types.UninitialisedField(self, 'SchmeNm', OrganisationIdentificationSchemeName2Choice, False)

	@SchmeNm.deleter
	def SchmeNm(self):
		del self._SchmeNm
		self._SchmeNm = base_types.UninitialisedField(self, 'SchmeNm', OrganisationIdentificationSchemeName2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=RestrictedFINXMax35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Issr', type=RestrictedFINXMax35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchmeNm', type=OrganisationIdentificationSchemeName2Choice, min=0, max=1, mutex_group=None, array=False),
	))