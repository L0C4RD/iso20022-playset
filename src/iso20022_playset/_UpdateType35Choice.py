from . import base_types
from ._SecurityAttributes12 import SecurityAttributes12

class UpdateType35Choice(base_types._BaseFieldType):

	__slots__ = ["_Del", "_Modfy", "_Add"]
	@property
	def Add(self):
		return self._Add

	@Add.setter
	def Add(self, value):
		self._Add = value if type(value) != base_types.auto else self.make_default("Add")

	@Add.deleter
	def Add(self):
		del self._Add
		self._Add = None

	@property
	def Del(self):
		return self._Del

	@Del.setter
	def Del(self, value):
		self._Del = value if type(value) != base_types.auto else self.make_default("Del")

	@Del.deleter
	def Del(self):
		del self._Del
		self._Del = None

	@property
	def Modfy(self):
		return self._Modfy

	@Modfy.setter
	def Modfy(self, value):
		self._Modfy = value if type(value) != base_types.auto else self.make_default("Modfy")

	@Modfy.deleter
	def Modfy(self):
		del self._Modfy
		self._Modfy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Add', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Del', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Modfy', type=SecurityAttributes12, min=0, max=1, mutex_group=1, array=False),
	))

