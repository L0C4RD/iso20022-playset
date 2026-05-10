from . import base_types
from .Max35Text import Max35Text

class GenericIdentification4(base_types._BaseFieldType):

	__slots__ = ["_Id", "_IdTp"]
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
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if type(value) != base_types.auto else self.make_default("IdTp")

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IdTp', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

