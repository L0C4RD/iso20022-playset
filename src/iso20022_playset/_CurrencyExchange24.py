from . import base_types
from ._Max35Text import Max35Text
from ._BaseOneRate import BaseOneRate
from ._PositiveNumber import PositiveNumber
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._ISODateTime import ISODateTime

class CurrencyExchange24(base_types._BaseFieldType):

	__slots__ = ["_UnitCcy", "_CtrctId", "_TrgtCcy", "_XchgRateBase", "_XchgRate", "_QtnDt", "_SrcCcy"]
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
	def TrgtCcy(self):
		return self._TrgtCcy

	@TrgtCcy.setter
	def TrgtCcy(self, value):
		self._TrgtCcy = value if type(value) != base_types.auto else self.make_default("TrgtCcy")

	@TrgtCcy.deleter
	def TrgtCcy(self):
		del self._TrgtCcy
		self._TrgtCcy = None

	@property
	def XchgRateBase(self):
		return self._XchgRateBase

	@XchgRateBase.setter
	def XchgRateBase(self, value):
		self._XchgRateBase = value if type(value) != base_types.auto else self.make_default("XchgRateBase")

	@XchgRateBase.deleter
	def XchgRateBase(self):
		del self._XchgRateBase
		self._XchgRateBase = None

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
	def QtnDt(self):
		return self._QtnDt

	@QtnDt.setter
	def QtnDt(self, value):
		self._QtnDt = value if type(value) != base_types.auto else self.make_default("QtnDt")

	@QtnDt.deleter
	def QtnDt(self):
		del self._QtnDt
		self._QtnDt = None

	@property
	def SrcCcy(self):
		return self._SrcCcy

	@SrcCcy.setter
	def SrcCcy(self, value):
		self._SrcCcy = value if type(value) != base_types.auto else self.make_default("SrcCcy")

	@SrcCcy.deleter
	def SrcCcy(self):
		del self._SrcCcy
		self._SrcCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UnitCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateBase', type=PositiveNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
	))

