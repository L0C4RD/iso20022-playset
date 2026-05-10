import base_types
import EnergyQuantityUnit2Choice
import TimePeriodDetails1
import Quantity47Choice
import WeekDay3Code
import AmountAndDirection106
import DurationType1Code
import DatePeriod1

class EnergyDeliveryAttribute10(base_types._BaseFieldType):

	__slots__ = ["_DlvryDt", "_DlvryIntrvl", "_WkDay", "_QtyUnit", "_PricTmIntrvlQty", "_DlvryCpcty", "_Drtn"]
	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if type(value) != auto else self.make_default("DlvryDt")

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = None

	@property
	def DlvryIntrvl(self):
		return self._DlvryIntrvl

	@DlvryIntrvl.setter
	def DlvryIntrvl(self, value):
		self._DlvryIntrvl = value if type(value) != auto else self.make_default("DlvryIntrvl")

	@DlvryIntrvl.deleter
	def DlvryIntrvl(self):
		del self._DlvryIntrvl
		self._DlvryIntrvl = None

	@property
	def WkDay(self):
		return self._WkDay

	@WkDay.setter
	def WkDay(self, value):
		self._WkDay = value if type(value) != auto else self.make_default("WkDay")

	@WkDay.deleter
	def WkDay(self):
		del self._WkDay
		self._WkDay = None

	@property
	def QtyUnit(self):
		return self._QtyUnit

	@QtyUnit.setter
	def QtyUnit(self, value):
		self._QtyUnit = value if type(value) != auto else self.make_default("QtyUnit")

	@QtyUnit.deleter
	def QtyUnit(self):
		del self._QtyUnit
		self._QtyUnit = None

	@property
	def PricTmIntrvlQty(self):
		return self._PricTmIntrvlQty

	@PricTmIntrvlQty.setter
	def PricTmIntrvlQty(self, value):
		self._PricTmIntrvlQty = value if type(value) != auto else self.make_default("PricTmIntrvlQty")

	@PricTmIntrvlQty.deleter
	def PricTmIntrvlQty(self):
		del self._PricTmIntrvlQty
		self._PricTmIntrvlQty = None

	@property
	def DlvryCpcty(self):
		return self._DlvryCpcty

	@DlvryCpcty.setter
	def DlvryCpcty(self, value):
		self._DlvryCpcty = value if type(value) != auto else self.make_default("DlvryCpcty")

	@DlvryCpcty.deleter
	def DlvryCpcty(self):
		del self._DlvryCpcty
		self._DlvryCpcty = None

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if type(value) != auto else self.make_default("Drtn")

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryDt', type=DatePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryIntrvl', type=TimePeriodDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='WkDay', type=WeekDay3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QtyUnit', type=EnergyQuantityUnit2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTmIntrvlQty', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryCpcty', type=Quantity47Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Drtn', type=DurationType1Code, min=0, max=1, mutex_group=None, array=False),
	))

