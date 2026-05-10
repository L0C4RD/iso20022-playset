from . import base_types
from ._BaseOneRate import BaseOneRate
from ._Max70Text import Max70Text
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._ISODateTime import ISODateTime
from ._Max40Text import Max40Text

class CurrencyExchange6(base_types._BaseFieldType):

	__slots__ = ["_UnitCcy", "_QtnDt", "_XchgRate", "_Cmnts", "_TrgtCcy", "_Desc", "_SrcCcy"]
	@property
	def Cmnts(self):
		return self._Cmnts

	@Cmnts.setter
	def Cmnts(self, value):
		self._Cmnts = value if type(value) != base_types.auto else self.make_default("Cmnts")

	@Cmnts.deleter
	def Cmnts(self):
		del self._Cmnts
		self._Cmnts = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

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
		base_types.FieldEntry(name='Cmnts', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtCcy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRate', type=BaseOneRate, min=1, max=1, mutex_group=None, array=False),
	))

