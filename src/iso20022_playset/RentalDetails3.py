from . import base_types
from .Max4NumericText import Max4NumericText
from .Max70Text import Max70Text
from .ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .ISODateTime import ISODateTime
from .PeriodUnit2Code import PeriodUnit2Code
from .ServiceStartEnd3 import ServiceStartEnd3

class RentalDetails3(base_types._BaseFieldType):

	__slots__ = ["_TmPrdUnit", "_DtTm", "_Start", "_TmPrdRate", "_Rtr", "_TmPrd", "_Id", "_Ccy"]
	@property
	def TmPrdUnit(self):
		return self._TmPrdUnit

	@TmPrdUnit.setter
	def TmPrdUnit(self, value):
		self._TmPrdUnit = value if type(value) != base_types.auto else self.make_default("TmPrdUnit")

	@TmPrdUnit.deleter
	def TmPrdUnit(self):
		del self._TmPrdUnit
		self._TmPrdUnit = None

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != base_types.auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def Start(self):
		return self._Start

	@Start.setter
	def Start(self, value):
		self._Start = value if type(value) != base_types.auto else self.make_default("Start")

	@Start.deleter
	def Start(self):
		del self._Start
		self._Start = None

	@property
	def TmPrdRate(self):
		return self._TmPrdRate

	@TmPrdRate.setter
	def TmPrdRate(self, value):
		self._TmPrdRate = value if type(value) != base_types.auto else self.make_default("TmPrdRate")

	@TmPrdRate.deleter
	def TmPrdRate(self):
		del self._TmPrdRate
		self._TmPrdRate = None

	@property
	def Rtr(self):
		return self._Rtr

	@Rtr.setter
	def Rtr(self, value):
		self._Rtr = value if type(value) != base_types.auto else self.make_default("Rtr")

	@Rtr.deleter
	def Rtr(self):
		del self._Rtr
		self._Rtr = None

	@property
	def TmPrd(self):
		return self._TmPrd

	@TmPrd.setter
	def TmPrd(self, value):
		self._TmPrd = value if type(value) != base_types.auto else self.make_default("TmPrd")

	@TmPrd.deleter
	def TmPrd(self):
		del self._TmPrd
		self._TmPrd = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='TmPrdUnit', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Start', type=ServiceStartEnd3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmPrdRate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rtr', type=ServiceStartEnd3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmPrd', type=PeriodUnit2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
	))

