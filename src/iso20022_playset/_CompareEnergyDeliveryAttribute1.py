from . import base_types
from .CompareAmountAndDirection3 import CompareAmountAndDirection3
from .CompareWeekDay1 import CompareWeekDay1
from .CompareEnergyQuantityUnit1 import CompareEnergyQuantityUnit1
from .CompareTimePeriod2 import CompareTimePeriod2
from .CompareDurationType1 import CompareDurationType1
from .CompareDatePeriod2 import CompareDatePeriod2
from .CompareLongFraction19DecimalNumber1 import CompareLongFraction19DecimalNumber1

class CompareEnergyDeliveryAttribute1(base_types._BaseFieldType):

	__slots__ = ["_NrgyDlvryIntrvl", "_NrgyDt", "_NrgyDrtn", "_NrgyDlvryCpcty", "_NrgyQtyUnit", "_NrgyPricTmIntrvlQty", "_NrgyWkDay"]
	@property
	def NrgyDlvryIntrvl(self):
		return self._NrgyDlvryIntrvl

	@NrgyDlvryIntrvl.setter
	def NrgyDlvryIntrvl(self, value):
		self._NrgyDlvryIntrvl = value if type(value) != base_types.auto else self.make_default("NrgyDlvryIntrvl")

	@NrgyDlvryIntrvl.deleter
	def NrgyDlvryIntrvl(self):
		del self._NrgyDlvryIntrvl
		self._NrgyDlvryIntrvl = None

	@property
	def NrgyDt(self):
		return self._NrgyDt

	@NrgyDt.setter
	def NrgyDt(self, value):
		self._NrgyDt = value if type(value) != base_types.auto else self.make_default("NrgyDt")

	@NrgyDt.deleter
	def NrgyDt(self):
		del self._NrgyDt
		self._NrgyDt = None

	@property
	def NrgyDrtn(self):
		return self._NrgyDrtn

	@NrgyDrtn.setter
	def NrgyDrtn(self, value):
		self._NrgyDrtn = value if type(value) != base_types.auto else self.make_default("NrgyDrtn")

	@NrgyDrtn.deleter
	def NrgyDrtn(self):
		del self._NrgyDrtn
		self._NrgyDrtn = None

	@property
	def NrgyDlvryCpcty(self):
		return self._NrgyDlvryCpcty

	@NrgyDlvryCpcty.setter
	def NrgyDlvryCpcty(self, value):
		self._NrgyDlvryCpcty = value if type(value) != base_types.auto else self.make_default("NrgyDlvryCpcty")

	@NrgyDlvryCpcty.deleter
	def NrgyDlvryCpcty(self):
		del self._NrgyDlvryCpcty
		self._NrgyDlvryCpcty = None

	@property
	def NrgyQtyUnit(self):
		return self._NrgyQtyUnit

	@NrgyQtyUnit.setter
	def NrgyQtyUnit(self, value):
		self._NrgyQtyUnit = value if type(value) != base_types.auto else self.make_default("NrgyQtyUnit")

	@NrgyQtyUnit.deleter
	def NrgyQtyUnit(self):
		del self._NrgyQtyUnit
		self._NrgyQtyUnit = None

	@property
	def NrgyPricTmIntrvlQty(self):
		return self._NrgyPricTmIntrvlQty

	@NrgyPricTmIntrvlQty.setter
	def NrgyPricTmIntrvlQty(self, value):
		self._NrgyPricTmIntrvlQty = value if type(value) != base_types.auto else self.make_default("NrgyPricTmIntrvlQty")

	@NrgyPricTmIntrvlQty.deleter
	def NrgyPricTmIntrvlQty(self):
		del self._NrgyPricTmIntrvlQty
		self._NrgyPricTmIntrvlQty = None

	@property
	def NrgyWkDay(self):
		return self._NrgyWkDay

	@NrgyWkDay.setter
	def NrgyWkDay(self, value):
		self._NrgyWkDay = value if type(value) != base_types.auto else self.make_default("NrgyWkDay")

	@NrgyWkDay.deleter
	def NrgyWkDay(self):
		del self._NrgyWkDay
		self._NrgyWkDay = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NrgyDlvryIntrvl', type=CompareTimePeriod2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrgyDt', type=CompareDatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyDrtn', type=CompareDurationType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyDlvryCpcty', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyQtyUnit', type=CompareEnergyQuantityUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyPricTmIntrvlQty', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyWkDay', type=CompareWeekDay1, min=0, max=None, mutex_group=None, array=True),
	))

