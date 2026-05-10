from . import base_types
from .Max350Text import Max350Text

class Addition2(base_types._BaseFieldType):

	__slots__ = ["_PropsdVal"]
	@property
	def PropsdVal(self):
		return self._PropsdVal

	@PropsdVal.setter
	def PropsdVal(self, value):
		self._PropsdVal = value if type(value) != auto else self.make_default("PropsdVal")

	@PropsdVal.deleter
	def PropsdVal(self):
		del self._PropsdVal
		self._PropsdVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PropsdVal', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

