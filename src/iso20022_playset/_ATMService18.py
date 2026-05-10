from . import base_types
from ._Max35Text import Max35Text

class ATMService18(base_types._BaseFieldType):

	__slots__ = ["_Labl", "_Id"]
	@property
	def Labl(self):
		return self._Labl

	@Labl.setter
	def Labl(self, value):
		self._Labl = value if type(value) != base_types.auto else self.make_default("Labl")

	@Labl.deleter
	def Labl(self):
		del self._Labl
		self._Labl = None

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
		base_types.FieldEntry(name='Labl', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

