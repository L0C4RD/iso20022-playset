# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Number
from . import PercentageRate

class RateOrAbsoluteValue1Choice(base_types._BaseFieldType):

	__slots__ = ["_AbsVal", "_RateVal"]
	@property
	def AbsVal(self):
		return self._AbsVal

	@AbsVal.setter
	def AbsVal(self, value):
		self._AbsVal = value if value is not None else base_types.UninitialisedField(self, 'AbsVal', Number, False)

	@AbsVal.deleter
	def AbsVal(self):
		del self._AbsVal
		self._AbsVal = base_types.UninitialisedField(self, 'AbsVal', Number, False)

	@property
	def RateVal(self):
		return self._RateVal

	@RateVal.setter
	def RateVal(self, value):
		self._RateVal = value if value is not None else base_types.UninitialisedField(self, 'RateVal', PercentageRate, False)

	@RateVal.deleter
	def RateVal(self):
		del self._RateVal
		self._RateVal = base_types.UninitialisedField(self, 'RateVal', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AbsVal', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateVal', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))