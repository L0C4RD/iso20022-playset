import base_types
import RateBasis1Code
import Max3Number

class InterestRateContractTerm2(base_types._BaseFieldType):

	__slots__ = ["_Unit", "_Val"]
	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Unit', type=RateBasis1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max3Number, min=1, max=1, mutex_group=None, array=False),
	))

