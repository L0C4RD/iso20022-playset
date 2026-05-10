from . import base_types
from .PercentageRate import PercentageRate
from .Number import Number

class RateOrAbsoluteValue1Choice(base_types._BaseFieldType):

	__slots__ = ["_RateVal", "_AbsVal"]
	@property
	def RateVal(self):
		return self._RateVal

	@RateVal.setter
	def RateVal(self, value):
		self._RateVal = value if type(value) != auto else self.make_default("RateVal")

	@RateVal.deleter
	def RateVal(self):
		del self._RateVal
		self._RateVal = None

	@property
	def AbsVal(self):
		return self._AbsVal

	@AbsVal.setter
	def AbsVal(self, value):
		self._AbsVal = value if type(value) != auto else self.make_default("AbsVal")

	@AbsVal.deleter
	def AbsVal(self):
		del self._AbsVal
		self._AbsVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RateVal', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AbsVal', type=Number, min=0, max=1, mutex_group=1, array=False),
	))

