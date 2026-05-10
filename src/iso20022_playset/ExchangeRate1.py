from . import base_types
from .BaseOneRate import BaseOneRate
from .ExchangeRateType1Code import ExchangeRateType1Code
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .Max35Text import Max35Text

class ExchangeRate1(base_types._BaseFieldType):

	__slots__ = ["_XchgRate", "_CtrctId", "_UnitCcy", "_RateTp"]
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
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if type(value) != base_types.auto else self.make_default("UnitCcy")

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RateTp', type=ExchangeRateType1Code, min=0, max=1, mutex_group=None, array=False),
	))

