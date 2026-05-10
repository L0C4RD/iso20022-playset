from . import base_types
from ._Max35Text import Max35Text

class Acquirer8(base_types._BaseFieldType):

	__slots__ = ["_Id", "_ApplVrsn"]
	@property
	def ApplVrsn(self):
		return self._ApplVrsn

	@ApplVrsn.setter
	def ApplVrsn(self, value):
		self._ApplVrsn = value if type(value) != base_types.auto else self.make_default("ApplVrsn")

	@ApplVrsn.deleter
	def ApplVrsn(self):
		del self._ApplVrsn
		self._ApplVrsn = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ApplVrsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

