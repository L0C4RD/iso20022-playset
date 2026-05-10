from . import base_types
from ._ClearingExceptionOrExemption3Choice import ClearingExceptionOrExemption3Choice
from ._ClearingPartyAndTime21Choice import ClearingPartyAndTime21Choice
from ._ClearingPartyAndTime22Choice import ClearingPartyAndTime22Choice

class Cleared23Choice(base_types._BaseFieldType):

	__slots__ = ["_Clrd", "_IntndToClear", "_NonClrd"]
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
	def IntndToClear(self):
		return self._IntndToClear

	@IntndToClear.setter
	def IntndToClear(self, value):
		self._IntndToClear = value if type(value) != base_types.auto else self.make_default("IntndToClear")

	@IntndToClear.deleter
	def IntndToClear(self):
		del self._IntndToClear
		self._IntndToClear = None

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
		base_types.FieldEntry(name='Clrd', type=ClearingPartyAndTime21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IntndToClear', type=ClearingPartyAndTime22Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonClrd', type=ClearingExceptionOrExemption3Choice, min=0, max=1, mutex_group=1, array=False),
	))

