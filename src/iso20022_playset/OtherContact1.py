from . import base_types
from .Max128Text import Max128Text
from .Max4Text import Max4Text

class OtherContact1(base_types._BaseFieldType):

	__slots__ = ["_Id", "_ChanlTp"]
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
	def ChanlTp(self):
		return self._ChanlTp

	@ChanlTp.setter
	def ChanlTp(self, value):
		self._ChanlTp = value if type(value) != base_types.auto else self.make_default("ChanlTp")

	@ChanlTp.deleter
	def ChanlTp(self):
		del self._ChanlTp
		self._ChanlTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max128Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChanlTp', type=Max4Text, min=1, max=1, mutex_group=None, array=False),
	))

