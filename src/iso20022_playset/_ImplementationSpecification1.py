from . import base_types
from .Max350Text import Max350Text
from .Max2048Text import Max2048Text

class ImplementationSpecification1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_Regy"]
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
	def Regy(self):
		return self._Regy

	@Regy.setter
	def Regy(self, value):
		self._Regy = value if type(value) != base_types.auto else self.make_default("Regy")

	@Regy.deleter
	def Regy(self):
		del self._Regy
		self._Regy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max2048Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Regy', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

