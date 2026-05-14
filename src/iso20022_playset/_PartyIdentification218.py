# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentification205Choice import PartyIdentification205Choice
from ._PartyRole6Choice import PartyRole6Choice

class PartyIdentification218(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Role"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Role(self):
		return self._Role

	@Role.setter
	def Role(self, value):
		self._Role = value if type(value) != base_types.auto else self.make_default("Role")

	@Role.deleter
	def Role(self):
		del self._Role
		self._Role = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification205Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Role', type=PartyRole6Choice, min=1, max=1, mutex_group=None, array=False),
	))