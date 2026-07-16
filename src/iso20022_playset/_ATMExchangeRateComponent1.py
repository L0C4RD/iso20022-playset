# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max256Text
from . import PercentageRate

class ATMExchangeRateComponent1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_PblshDt", "_XchgRate"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max256Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max256Text, False)

	@property
	def PblshDt(self):
		return self._PblshDt

	@PblshDt.setter
	def PblshDt(self, value):
		self._PblshDt = value if value is not None else base_types.UninitialisedField(self, 'PblshDt', ISODateTime, False)

	@PblshDt.deleter
	def PblshDt(self):
		del self._PblshDt
		self._PblshDt = base_types.UninitialisedField(self, 'PblshDt', ISODateTime, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', PercentageRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblshDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))