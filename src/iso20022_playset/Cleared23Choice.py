import base_types
import ClearingPartyAndTime22Choice
import ClearingExceptionOrExemption3Choice
import ClearingPartyAndTime21Choice

class Cleared23Choice(base_types._BaseFieldType):

	__slots__ = ["_IntndToClear", "_Clrd", "_NonClrd"]
	@property
	def IntndToClear(self):
		return self._IntndToClear

	@IntndToClear.setter
	def IntndToClear(self, value):
		self._IntndToClear = value if type(value) != auto else self.make_default("IntndToClear")

	@IntndToClear.deleter
	def IntndToClear(self):
		del self._IntndToClear
		self._IntndToClear = None

	@property
	def Clrd(self):
		return self._Clrd

	@Clrd.setter
	def Clrd(self, value):
		self._Clrd = value if type(value) != auto else self.make_default("Clrd")

	@Clrd.deleter
	def Clrd(self):
		del self._Clrd
		self._Clrd = None

	@property
	def NonClrd(self):
		return self._NonClrd

	@NonClrd.setter
	def NonClrd(self, value):
		self._NonClrd = value if type(value) != auto else self.make_default("NonClrd")

	@NonClrd.deleter
	def NonClrd(self):
		del self._NonClrd
		self._NonClrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntndToClear', type=ClearingPartyAndTime22Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Clrd', type=ClearingPartyAndTime21Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NonClrd', type=ClearingExceptionOrExemption3Choice, min=0, max=1, mutex_group=1, array=False),
	))

