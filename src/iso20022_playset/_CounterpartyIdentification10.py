# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralRole1Code
from . import OrganisationIdentification15Choice

class CounterpartyIdentification10(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Sd"]
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
	def Sd(self):
		return self._Sd

	@Sd.setter
	def Sd(self, value):
		self._Sd = value if value is not None else base_types.UninitialisedField(self, 'Sd', CollateralRole1Code, False)

	@Sd.deleter
	def Sd(self):
		del self._Sd
		self._Sd = base_types.UninitialisedField(self, 'Sd', CollateralRole1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=OrganisationIdentification15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sd', type=CollateralRole1Code, min=0, max=1, mutex_group=None, array=False),
	))