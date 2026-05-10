from . import base_types
from ._Max3Number import Max3Number
from ._Frequency13Code import Frequency13Code

class InterestRateContractTerm4(base_types._BaseFieldType):

	__slots__ = ["_Val", "_Unit"]
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
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Val', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Unit', type=Frequency13Code, min=0, max=1, mutex_group=None, array=False),
	))

