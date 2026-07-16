# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BaseOneRate
from . import ExchangeRateOrPercentage1Choice
from . import ISODateTime

class CurrencyExchange20(base_types._BaseFieldType):

	__slots__ = ["_HghLmt", "_LwLmt", "_QtdCcy", "_QtnDt", "_XchgRate"]
	@property
	def HghLmt(self):
		return self._HghLmt

	@HghLmt.setter
	def HghLmt(self, value):
		self._HghLmt = value if value is not None else base_types.UninitialisedField(self, 'HghLmt', ExchangeRateOrPercentage1Choice, False)

	@HghLmt.deleter
	def HghLmt(self):
		del self._HghLmt
		self._HghLmt = base_types.UninitialisedField(self, 'HghLmt', ExchangeRateOrPercentage1Choice, False)

	@property
	def LwLmt(self):
		return self._LwLmt

	@LwLmt.setter
	def LwLmt(self, value):
		self._LwLmt = value if value is not None else base_types.UninitialisedField(self, 'LwLmt', ExchangeRateOrPercentage1Choice, False)

	@LwLmt.deleter
	def LwLmt(self):
		del self._LwLmt
		self._LwLmt = base_types.UninitialisedField(self, 'LwLmt', ExchangeRateOrPercentage1Choice, False)

	@property
	def QtdCcy(self):
		return self._QtdCcy

	@QtdCcy.setter
	def QtdCcy(self, value):
		self._QtdCcy = value if value is not None else base_types.UninitialisedField(self, 'QtdCcy', ActiveOrHistoricCurrencyCode, False)

	@QtdCcy.deleter
	def QtdCcy(self):
		del self._QtdCcy
		self._QtdCcy = base_types.UninitialisedField(self, 'QtdCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if value is not None else base_types.UninitialisedField(self, 'QtnDt', ISODateTime, False)

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = base_types.UninitialisedField(self, 'QtnDt', ISODateTime, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOneRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HghLmt', type=ExchangeRateOrPercentage1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LwLmt', type=ExchangeRateOrPercentage1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtdCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))