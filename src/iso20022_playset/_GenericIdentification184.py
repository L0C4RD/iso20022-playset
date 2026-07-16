# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max100Text
from . import Max210Text

class GenericIdentification184(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Src"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max210Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max210Text, False)

	@property
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if value is not None else base_types.UninitialisedField(self, 'Src', Max100Text, False)

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = base_types.UninitialisedField(self, 'Src', Max100Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max210Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Src', type=Max100Text, min=1, max=1, mutex_group=None, array=False),
	))