import base_types
import PercentageRate
import ISODateTime
import Max256Text

class ATMExchangeRateComponent1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_XchgRate", "_PblshDt"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	@property
	def PblshDt(self):
		return self._PblshDt

	@PblshDt.setter
	def PblshDt(self, value):
		self._PblshDt = value if type(value) != auto else self.make_default("PblshDt")

	@PblshDt.deleter
	def PblshDt(self):
		del self._PblshDt
		self._PblshDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PblshDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

