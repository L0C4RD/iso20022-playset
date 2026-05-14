# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._BaseOne18Rate import BaseOne18Rate
from ._ExchangeRateBasis1Choice import ExchangeRateBasis1Choice
from ._ISODateTime import ISODateTime

class CurrencyExchange22(base_types._BaseFieldType):

	__slots__ = ["_DlvrblCrossCcy", "_FwdXchgRate", "_FxgDt", "_XchgRate", "_XchgRateBsis"]
	@property
	def DlvrblCrossCcy(self):
		return self._DlvrblCrossCcy

	@DlvrblCrossCcy.setter
	def DlvrblCrossCcy(self, value):
		self._DlvrblCrossCcy = value if type(value) != base_types.auto else self.make_default("DlvrblCrossCcy")

	@DlvrblCrossCcy.deleter
	def DlvrblCrossCcy(self):
		del self._DlvrblCrossCcy
		self._DlvrblCrossCcy = None

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
	def XchgRateBsis(self):
		return self._XchgRateBsis

	@XchgRateBsis.setter
	def XchgRateBsis(self, value):
		self._XchgRateBsis = value if type(value) != base_types.auto else self.make_default("XchgRateBsis")

	@XchgRateBsis.deleter
	def XchgRateBsis(self):
		del self._XchgRateBsis
		self._XchgRateBsis = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvrblCrossCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FwdXchgRate', type=BaseOne18Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FxgDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOne18Rate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateBsis', type=ExchangeRateBasis1Choice, min=0, max=1, mutex_group=None, array=False),
	))