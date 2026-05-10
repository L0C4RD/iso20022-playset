from . import base_types
from .Max50Text import Max50Text

class CompareMax50Text1(base_types._BaseFieldType):

	__slots__ = ["_Val2", "_Val1"]
	@property
	def Val2(self):
		return self._Val2

	@Val2.setter
	def Val2(self, value):
		self._Val2 = value if type(value) != auto else self.make_default("Val2")

	@Val2.deleter
	def Val2(self):
		del self._Val2
		self._Val2 = None

	@property
	def Val1(self):
		return self._Val1

	@Val1.setter
	def Val1(self, value):
		self._Val1 = value if type(value) != auto else self.make_default("Val1")

	@Val1.deleter
	def Val1(self):
		del self._Val1
		self._Val1 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val2', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val1', type=Max50Text, min=0, max=1, mutex_group=None, array=False),
	))

