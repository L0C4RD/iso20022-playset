# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class Acquirer8(base_types._BaseFieldType):

	__slots__ = ["_ApplVrsn", "_Id"]
	@property
	def ApplVrsn(self):
		return self._ApplVrsn

	@ApplVrsn.setter
	def ApplVrsn(self, value):
		self._ApplVrsn = value if value is not None else base_types.UninitialisedField(self, 'ApplVrsn', Max35Text, False)

	@ApplVrsn.deleter
	def ApplVrsn(self):
		del self._ApplVrsn
		self._ApplVrsn = base_types.UninitialisedField(self, 'ApplVrsn', Max35Text, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApplVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))