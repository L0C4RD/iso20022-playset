from . import base_types
from .Number import Number

class TimeFrame8Choice(base_types._BaseFieldType):

	__slots__ = ["_TPlus", "_RPlus"]
	@property
	def TPlus(self):
		return self._TPlus

	@TPlus.setter
	def TPlus(self, value):
		self._TPlus = value if type(value) != base_types.auto else self.make_default("TPlus")

	@TPlus.deleter
	def TPlus(self):
		del self._TPlus
		self._TPlus = None

	@property
	def RPlus(self):
		return self._RPlus

	@RPlus.setter
	def RPlus(self, value):
		self._RPlus = value if type(value) != base_types.auto else self.make_default("RPlus")

	@RPlus.deleter
	def RPlus(self):
		del self._RPlus
		self._RPlus = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TPlus', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RPlus', type=Number, min=0, max=1, mutex_group=1, array=False),
	))

