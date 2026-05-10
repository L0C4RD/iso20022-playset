from . import base_types
from .Max350Text import Max350Text

class Replacement2(base_types._BaseFieldType):

	__slots__ = ["_CurVal", "_PropsdVal"]
	@property
	def CurVal(self):
		return self._CurVal

	@CurVal.setter
	def CurVal(self, value):
		self._CurVal = value if type(value) != base_types.auto else self.make_default("CurVal")

	@CurVal.deleter
	def CurVal(self):
		del self._CurVal
		self._CurVal = None

	@property
	def PropsdVal(self):
		return self._PropsdVal

	@PropsdVal.setter
	def PropsdVal(self, value):
		self._PropsdVal = value if type(value) != base_types.auto else self.make_default("PropsdVal")

	@PropsdVal.deleter
	def PropsdVal(self):
		del self._PropsdVal
		self._PropsdVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CurVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PropsdVal', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))

