from . import base_types
import ActiveOrHistoricCurrencyCode
import ExchangeRateOrPercentage1Choice
import BaseOneRate
import ISODateTime

class CurrencyExchange20(base_types._BaseFieldType):

	__slots__ = ["_QtdCcy", "_XchgRate", "_LwLmt", "_HghLmt", "_QtnDt"]
	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if type(value) != auto else self.make_default("QtdCcy")

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = None

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
	def LwLmt(self):
		return self._LwLmt

	@LwLmt.setter
	def LwLmt(self, value):
		self._LwLmt = value if type(value) != auto else self.make_default("LwLmt")

	@LwLmt.deleter
	def LwLmt(self):
		del self._LwLmt
		self._LwLmt = None

	@property
	def HghLmt(self):
		return self._HghLmt

	@HghLmt.setter
	def HghLmt(self, value):
		self._HghLmt = value if type(value) != auto else self.make_default("HghLmt")

	@HghLmt.deleter
	def HghLmt(self):
		del self._HghLmt
		self._HghLmt = None

	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if type(value) != auto else self.make_default("QtnDt")

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='QtdCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwLmt', type=ExchangeRateOrPercentage1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HghLmt', type=ExchangeRateOrPercentage1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
	))

