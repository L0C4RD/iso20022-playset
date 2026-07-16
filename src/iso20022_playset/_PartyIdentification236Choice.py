# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NaturalPersonIdentification2
from . import OrganisationIdentification15Choice

class PartyIdentification236Choice(base_types._BaseFieldType):

	__slots__ = ["_Lgl", "_Ntrl"]
	@property
	def Lgl(self):
		return self._Lgl

	@Lgl.setter
	def Lgl(self, value):
		self._Lgl = value if value is not None else base_types.UninitialisedField(self, 'Lgl', OrganisationIdentification15Choice, False)

	@Lgl.deleter
	def Lgl(self):
		del self._Lgl
		self._Lgl = base_types.UninitialisedField(self, 'Lgl', OrganisationIdentification15Choice, False)

	@property
	def Ntrl(self):
		return self._Ntrl

	@Ntrl.setter
	def Ntrl(self, value):
		self._Ntrl = value if value is not None else base_types.UninitialisedField(self, 'Ntrl', NaturalPersonIdentification2, False)

	@Ntrl.deleter
	def Ntrl(self):
		del self._Ntrl
		self._Ntrl = base_types.UninitialisedField(self, 'Ntrl', NaturalPersonIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Lgl', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Ntrl', type=NaturalPersonIdentification2, min=0, max=1, mutex_group=1, array=False),
	))