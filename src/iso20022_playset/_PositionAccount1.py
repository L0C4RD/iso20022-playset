# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentification118Choice import PartyIdentification118Choice

class PositionAccount1(base_types._BaseFieldType):

	__slots__ = ["_Id"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
	))