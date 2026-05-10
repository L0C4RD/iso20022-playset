from . import base_types
from .YesNoIndicator import YesNoIndicator
from .Max35Text import Max35Text

class DataBaseCheck1(base_types._BaseFieldType):

	__slots__ = ["_DBChck", "_Id"]
	@property
	def DBChck(self):
		return self._DBChck

	@DBChck.setter
	def DBChck(self, value):
		self._DBChck = value if type(value) != base_types.auto else self.make_default("DBChck")

	@DBChck.deleter
	def DBChck(self):
		del self._DBChck
		self._DBChck = None

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
		base_types.FieldEntry(name='DBChck', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

