from . import base_types
from ._Max34Text import Max34Text

class SimpleIdentificationInformation2(base_types._BaseFieldType):

	__slots__ = ["_Id"]
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
		base_types.FieldEntry(name='Id', type=Max34Text, min=1, max=1, mutex_group=None, array=False),
	))

