# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AnyBICDec2014Identifier import AnyBICDec2014Identifier
from ._LEIIdentifier import LEIIdentifier

class PlaceOfClearingIdentification2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_LEI"]
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
	def LEI(self):
		return self._LEI

	@LEI.setter
	def LEI(self, value):
		self._LEI = value if type(value) != base_types.auto else self.make_default("LEI")

	@LEI.deleter
	def LEI(self):
		del self._LEI
		self._LEI = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=AnyBICDec2014Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LEI', type=LEIIdentifier, min=0, max=1, mutex_group=None, array=False),
	))