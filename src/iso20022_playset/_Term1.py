from . import base_types
from ._RateOrAbsoluteValue1Choice import RateOrAbsoluteValue1Choice
from ._Operator1Code import Operator1Code

class Term1(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Oprtr"]
	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != base_types.auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def Oprtr(self):
		return self._Oprtr

	@Oprtr.setter
	def Oprtr(self, value):
		self._Oprtr = value if type(value) != base_types.auto else self.make_default("Oprtr")

	@Oprtr.deleter
	def Oprtr(self):
		del self._Oprtr
		self._Oprtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=RateOrAbsoluteValue1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Oprtr', type=Operator1Code, min=1, max=1, mutex_group=None, array=False),
	))

