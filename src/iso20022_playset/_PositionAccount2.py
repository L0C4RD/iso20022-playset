# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification165
from . import Position1

class PositionAccount2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Pos"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', GenericIdentification165, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', GenericIdentification165, False)

	@property
	def Pos(self):
		return self._Pos

	@Pos.setter
	def Pos(self, value):
		self._Pos = value if value is not None else base_types.UninitialisedField(self, 'Pos', Position1, True)

	@Pos.deleter
	def Pos(self):
		del self._Pos
		self._Pos = base_types.UninitialisedField(self, 'Pos', Position1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pos', type=Position1, min=1, max=None, mutex_group=None, array=True),
	))