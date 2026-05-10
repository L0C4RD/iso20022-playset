from . import base_types
from ._NoReasonCode import NoReasonCode

class Cleared4Choice(base_types._BaseFieldType):

	__slots__ = ["_NonClrd", "_Clrd"]
	@property
	def Clrd(self):
		return self._Clrd

	@Clrd.setter
	def Clrd(self, value):
		self._Clrd = value if type(value) != base_types.auto else self.make_default("Clrd")

	@Clrd.deleter
	def Clrd(self):
		del self._Clrd
		self._Clrd = None

	@property
	def NonClrd(self):
		return self._NonClrd

	@NonClrd.setter
	def NonClrd(self, value):
		self._NonClrd = value if type(value) != base_types.auto else self.make_default("NonClrd")

	@NonClrd.deleter
	def NonClrd(self):
		del self._NonClrd
		self._NonClrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Clrd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonClrd', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

