from . import base_types
from ._FATCAStatus2Choice import FATCAStatus2Choice
from ._FATCASource1Choice import FATCASource1Choice

class FATCAStatus2(base_types._BaseFieldType):

	__slots__ = ["_Src", "_Tp"]
	@property
	def Src(self):
		return self._Src

	@Src.setter
	def Src(self, value):
		self._Src = value if type(value) != base_types.auto else self.make_default("Src")

	@Src.deleter
	def Src(self):
		del self._Src
		self._Src = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Src', type=FATCASource1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FATCAStatus2Choice, min=1, max=1, mutex_group=None, array=False),
	))

