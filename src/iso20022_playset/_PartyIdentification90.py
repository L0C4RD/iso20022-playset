# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import PartyIdentificationType1Code

class PartyIdentification90(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdTp"]
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

	@property
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if value is not None else base_types.UninitialisedField(self, 'IdTp', PartyIdentificationType1Code, False)

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = base_types.UninitialisedField(self, 'IdTp', PartyIdentificationType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdTp', type=PartyIdentificationType1Code, min=1, max=1, mutex_group=None, array=False),
	))