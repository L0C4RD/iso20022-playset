from . import base_types
from ._Max100Text import Max100Text
from ._Max210Text import Max210Text

class GenericIdentification184(base_types._BaseFieldType):

	__slots__ = ["_Src", "_Id"]
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
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if type(value) != base_types.auto else self.make_default("Src")

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max210Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Src', type=Max100Text, min=1, max=1, mutex_group=None, array=False),
	))

