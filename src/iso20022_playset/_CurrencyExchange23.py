# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BaseOne18Rate
from . import ExchangeRateBasis1Choice
from . import ISODateTime

class CurrencyExchange23(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_FwdXchgRate", "_FxgDt", "_XchgRate", "_XchgRateBsis"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@property
	def FwdXchgRate(self):
		return self._FwdXchgRate

	@FwdXchgRate.setter
	def FwdXchgRate(self, value):
		self._FwdXchgRate = value if value is not None else base_types.UninitialisedField(self, 'FwdXchgRate', BaseOne18Rate, False)

	@FwdXchgRate.deleter
	def FwdXchgRate(self):
		del self._FwdXchgRate
		self._FwdXchgRate = base_types.UninitialisedField(self, 'FwdXchgRate', BaseOne18Rate, False)

	@property
	def FxgDt(self):
		return self._FxgDt

	@FxgDt.setter
	def FxgDt(self, value):
		self._FxgDt = value if value is not None else base_types.UninitialisedField(self, 'FxgDt', ISODateTime, False)

	@FxgDt.deleter
	def FxgDt(self):
		del self._FxgDt
		self._FxgDt = base_types.UninitialisedField(self, 'FxgDt', ISODateTime, False)

	@property
	def XchgRate(self):
		return self._XchgRate

	@XchgRate.setter
	def XchgRate(self, value):
		self._XchgRate = value if value is not None else base_types.UninitialisedField(self, 'XchgRate', BaseOne18Rate, False)

	@XchgRate.deleter
	def XchgRate(self):
		del self._XchgRate
		self._XchgRate = base_types.UninitialisedField(self, 'XchgRate', BaseOne18Rate, False)

	@property
	def XchgRateBsis(self):
		return self._XchgRateBsis

	@XchgRateBsis.setter
	def XchgRateBsis(self, value):
		self._XchgRateBsis = value if value is not None else base_types.UninitialisedField(self, 'XchgRateBsis', ExchangeRateBasis1Choice, False)

	@XchgRateBsis.deleter
	def XchgRateBsis(self):
		del self._XchgRateBsis
		self._XchgRateBsis = base_types.UninitialisedField(self, 'XchgRateBsis', ExchangeRateBasis1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdXchgRate', type=BaseOne18Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOne18Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateBsis', type=ExchangeRateBasis1Choice, min=0, max=1, mutex_group=None, array=False),
	))