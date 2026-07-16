# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import BaseOneRate
from . import ISODateTime
from . import Max35Text
from . import PositiveNumber

class CurrencyExchange24(base_types._BaseFieldType):

	__slots__ = ["_CtrctId", "_QtnDt", "_SrcCcy", "_TrgtCcy", "_UnitCcy", "_XchgRate", "_XchgRateBase"]
	@property
	def CtrctId(self):
		return self._CtrctId

	@CtrctId.setter
	def CtrctId(self, value):
		self._CtrctId = value if value is not None else base_types.UninitialisedField(self, 'CtrctId', Max35Text, False)

	@CtrctId.deleter
	def CtrctId(self):
		del self._CtrctId
		self._CtrctId = base_types.UninitialisedField(self, 'CtrctId', Max35Text, False)

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
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if value is not None else base_types.UninitialisedField(self, 'SrcCcy', ActiveOrHistoricCurrencyCode, False)

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = base_types.UninitialisedField(self, 'SrcCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if value is not None else base_types.UninitialisedField(self, 'TrgtCcy', ActiveOrHistoricCurrencyCode, False)

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = base_types.UninitialisedField(self, 'TrgtCcy', ActiveOrHistoricCurrencyCode, False)

	@property
	def UnitCcy(self):
		return self._UnitCcy

	@UnitCcy.setter
	def UnitCcy(self, value):
		self._UnitCcy = value if value is not None else base_types.UninitialisedField(self, 'UnitCcy', ActiveOrHistoricCurrencyCode, False)

	@UnitCcy.deleter
	def UnitCcy(self):
		del self._UnitCcy
		self._UnitCcy = base_types.UninitialisedField(self, 'UnitCcy', ActiveOrHistoricCurrencyCode, False)

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

	@property
	def XchgRateBase(self):
		return self._XchgRateBase

	@XchgRateBase.setter
	def XchgRateBase(self, value):
		self._XchgRateBase = value if value is not None else base_types.UninitialisedField(self, 'XchgRateBase', PositiveNumber, False)

	@XchgRateBase.deleter
	def XchgRateBase(self):
		del self._XchgRateBase
		self._XchgRateBase = base_types.UninitialisedField(self, 'XchgRateBase', PositiveNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateBase', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
	))