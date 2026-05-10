import base_types
import BaseOneRate
import ExchangeRateType1Code
import Max35Text

class ExchangeRateInformation1(base_types._BaseFieldType):

	__slots__ = ["_XchgRate", "_RateTp", "_CtrctId"]
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
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	@property
	def CtrctId(self):
		return self._CtrctId

	@CtrctId.setter
	def CtrctId(self, value):
		self._CtrctId = value if type(value) != auto else self.make_default("CtrctId")

	@CtrctId.deleter
	def CtrctId(self):
		del self._CtrctId
		self._CtrctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=ExchangeRateType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

