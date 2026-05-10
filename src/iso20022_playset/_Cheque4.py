from . import base_types
from ._NameAndAddress5 import NameAndAddress5

class Cheque4(base_types._BaseFieldType):

	__slots__ = ["_PyeeId"]
	@property
	def PyeeId(self):
		return self._PyeeId

	@PyeeId.setter
	def PyeeId(self, value):
		self._PyeeId = value if type(value) != base_types.auto else self.make_default("PyeeId")

	@PyeeId.deleter
	def PyeeId(self):
		del self._PyeeId
		self._PyeeId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PyeeId', type=NameAndAddress5, min=1, max=1, mutex_group=None, array=False),
	))

