from . import base_types
from .DurationType1Code import DurationType1Code
from .EnergyQuantityUnit2Choice import EnergyQuantityUnit2Choice
from .WeekDay3Code import WeekDay3Code
from .AmountAndDirection106 import AmountAndDirection106
from .TimePeriodDetails1 import TimePeriodDetails1
from .DatePeriod1 import DatePeriod1
from .Quantity47Choice import Quantity47Choice

class EnergyDeliveryAttribute10(base_types._BaseFieldType):

	__slots__ = ["_Drtn", "_DlvryDt", "_DlvryCpcty", "_DlvryIntrvl", "_PricTmIntrvlQty", "_WkDay", "_QtyUnit"]
	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != base_types.auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if type(value) != base_types.auto else self.make_default("DlvryDt")

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = None

	@property
	def DlvryCpcty(self):
		return self._DlvryCpcty

	@DlvryCpcty.setter
	def DlvryCpcty(self, value):
		self._DlvryCpcty = value if type(value) != base_types.auto else self.make_default("DlvryCpcty")

	@DlvryCpcty.deleter
	def DlvryCpcty(self):
		del self._DlvryCpcty
		self._DlvryCpcty = None

	@property
	def DlvryIntrvl(self):
		return self._DlvryIntrvl

	@DlvryIntrvl.setter
	def DlvryIntrvl(self, value):
		self._DlvryIntrvl = value if type(value) != base_types.auto else self.make_default("DlvryIntrvl")

	@DlvryIntrvl.deleter
	def DlvryIntrvl(self):
		del self._DlvryIntrvl
		self._DlvryIntrvl = None

	@property
	def PricTmIntrvlQty(self):
		return self._PricTmIntrvlQty

	@PricTmIntrvlQty.setter
	def PricTmIntrvlQty(self, value):
		self._PricTmIntrvlQty = value if type(value) != base_types.auto else self.make_default("PricTmIntrvlQty")

	@PricTmIntrvlQty.deleter
	def PricTmIntrvlQty(self):
		del self._PricTmIntrvlQty
		self._PricTmIntrvlQty = None

	@property
	def WkDay(self):
		return self._WkDay

	@WkDay.setter
	def WkDay(self, value):
		self._WkDay = value if type(value) != base_types.auto else self.make_default("WkDay")

	@WkDay.deleter
	def WkDay(self):
		del self._WkDay
		self._WkDay = None

	@property
	def QtyUnit(self):
		return self._QtyUnit

	@QtyUnit.setter
	def QtyUnit(self, value):
		self._QtyUnit = value if type(value) != base_types.auto else self.make_default("QtyUnit")

	@QtyUnit.deleter
	def QtyUnit(self):
		del self._QtyUnit
		self._QtyUnit = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Drtn', type=DurationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryDt', type=DatePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryCpcty', type=Quantity47Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryIntrvl', type=TimePeriodDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PricTmIntrvlQty', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WkDay', type=WeekDay3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyUnit', type=EnergyQuantityUnit2Choice, min=0, max=1, mutex_group=None, array=False),
	))

