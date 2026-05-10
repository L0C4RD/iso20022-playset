from . import base_types
from ._OptionNumber1Code import OptionNumber1Code
from ._Exact3NumericText import Exact3NumericText

class OptionNumber1Choice(base_types._BaseFieldType):

	__slots__ = ["_Nb", "_Cd"]
	@property
	def Nb(self):
		return self._Nb

	@Nb.setter
	def Nb(self, value):
		self._Nb = value if type(value) != base_types.auto else self.make_default("Nb")

	@Nb.deleter
	def Nb(self):
		del self._Nb
		self._Nb = None

	@property
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nb', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Cd', type=OptionNumber1Code, min=0, max=1, mutex_group=1, array=False),
	))

