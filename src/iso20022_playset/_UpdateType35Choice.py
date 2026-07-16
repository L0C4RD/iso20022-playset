# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SecurityAttributes12

class UpdateType35Choice(base_types._BaseFieldType):

	__slots__ = ["_Add", "_Del", "_Modfy"]
	@property
	def Add(self):
		return self._Add

	@Add.setter
	def Add(self, value):
		self._Add = value if value is not None else base_types.UninitialisedField(self, 'Add', SecurityAttributes12, False)

	@Add.deleter
	def Add(self):
		del self._Add
		self._Add = base_types.UninitialisedField(self, 'Add', SecurityAttributes12, False)

	@property
	def Del(self):
		return self._Del

	@Del.setter
	def Del(self, value):
		self._Del = value if value is not None else base_types.UninitialisedField(self, 'Del', SecurityAttributes12, False)

	@Del.deleter
	def Del(self):
		del self._Del
		self._Del = base_types.UninitialisedField(self, 'Del', SecurityAttributes12, False)

	@property
	def Modfy(self):
		return self._Modfy

	@Modfy.setter
	def Modfy(self, value):
		self._Modfy = value if value is not None else base_types.UninitialisedField(self, 'Modfy', SecurityAttributes12, False)

	@Modfy.deleter
	def Modfy(self):
		del self._Modfy
		self._Modfy = base_types.UninitialisedField(self, 'Modfy', SecurityAttributes12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Add', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Del', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Modfy', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
	))