from . import base_types
from ._Max35Text import Max35Text
from ._BaseOneRate import BaseOneRate
from ._ExchangeRateType1Code import ExchangeRateType1Code

class ExchangeRateInformation1(base_types._BaseFieldType):

	__slots__ = ["_RateTp", "_CtrctId", "_XchgRate"]
	@property
	def CtrctId(self):
		return self._CtrctId

	@CtrctId.setter
	def CtrctId(self, value):
		self._CtrctId = value if type(value) != base_types.auto else self.make_default("CtrctId")

	@CtrctId.deleter
	def CtrctId(self):
		del self._CtrctId
		self._CtrctId = None

	@property
	def RateTp(self):
		return self._RateTp

	@RateTp.setter
	def RateTp(self, value):
		self._RateTp = value if type(value) != base_types.auto else self.make_default("RateTp")

	@RateTp.deleter
	def RateTp(self):
		del self._RateTp
		self._RateTp = None

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if type(value) != base_types.auto else self.make_default("XchgRate")

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=ExchangeRateType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

