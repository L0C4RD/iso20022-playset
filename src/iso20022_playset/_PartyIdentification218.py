# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification205Choice
from . import PartyRole6Choice

class PartyIdentification218(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Role"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', PartyIdentification205Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', PartyIdentification205Choice, False)

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if value is not None else base_types.UninitialisedField(self, 'Role', PartyRole6Choice, False)

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = base_types.UninitialisedField(self, 'Role', PartyRole6Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification205Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=PartyRole6Choice, min=1, max=1, mutex_group=None, array=False),
	))