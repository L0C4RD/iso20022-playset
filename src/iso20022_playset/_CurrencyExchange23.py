from . import base_types
from .ISODateTime import ISODateTime
from .BaseOne18Rate import BaseOne18Rate
from .ExchangeRateBasis1Choice import ExchangeRateBasis1Choice
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class CurrencyExchange23(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_FxgDt", "_XchgRateBsis", "_XchgRate", "_FwdXchgRate"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def FxgDt(self):
		return self._FxgDt

	@FxgDt.setter
	def FxgDt(self, value):
		self._FxgDt = value if type(value) != base_types.auto else self.make_default("FxgDt")

	@FxgDt.deleter
	def FxgDt(self):
		del self._FxgDt
		self._FxgDt = None

	@property
	def XchgRateBsis(self):
		return self._XchgRateBsis

	@XchgRateBsis.setter
	def XchgRateBsis(self, value):
		self._XchgRateBsis = value if type(value) != base_types.auto else self.make_default("XchgRateBsis")

	@XchgRateBsis.deleter
	def XchgRateBsis(self):
		del self._XchgRateBsis
		self._XchgRateBsis = None

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
	def FwdXchgRate(self):
		return self._FwdXchgRate

	@FwdXchgRate.setter
	def FwdXchgRate(self, value):
		self._FwdXchgRate = value if type(value) != base_types.auto else self.make_default("FwdXchgRate")

	@FwdXchgRate.deleter
	def FwdXchgRate(self):
		del self._FwdXchgRate
		self._FwdXchgRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateBsis', type=ExchangeRateBasis1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOne18Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdXchgRate', type=BaseOne18Rate, min=0, max=1, mutex_group=None, array=False),
	))

