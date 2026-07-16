# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection106
from . import DatePeriod1
from . import DurationType1Code
from . import EnergyQuantityUnit2Choice
from . import Quantity47Choice
from . import TimePeriodDetails1
from . import WeekDay3Code

class EnergyDeliveryAttribute10(base_types._BaseFieldType):

	__slots__ = ["_DlvryCpcty", "_DlvryDt", "_DlvryIntrvl", "_Drtn", "_PricTmIntrvlQty", "_QtyUnit", "_WkDay"]
	@property
	def DlvryCpcty(self):
		return self._DlvryCpcty

	@DlvryCpcty.setter
	def DlvryCpcty(self, value):
		self._DlvryCpcty = value if value is not None else base_types.UninitialisedField(self, 'DlvryCpcty', Quantity47Choice, False)

	@DlvryCpcty.deleter
	def DlvryCpcty(self):
		del self._DlvryCpcty
		self._DlvryCpcty = base_types.UninitialisedField(self, 'DlvryCpcty', Quantity47Choice, False)

	@property
	def DlvryDt(self):
		return self._DlvryDt

	@DlvryDt.setter
	def DlvryDt(self, value):
		self._DlvryDt = value if value is not None else base_types.UninitialisedField(self, 'DlvryDt', DatePeriod1, False)

	@DlvryDt.deleter
	def DlvryDt(self):
		del self._DlvryDt
		self._DlvryDt = base_types.UninitialisedField(self, 'DlvryDt', DatePeriod1, False)

	@property
	def DlvryIntrvl(self):
		return self._DlvryIntrvl

	@DlvryIntrvl.setter
	def DlvryIntrvl(self, value):
		self._DlvryIntrvl = value if value is not None else base_types.UninitialisedField(self, 'DlvryIntrvl', TimePeriodDetails1, True)

	@DlvryIntrvl.deleter
	def DlvryIntrvl(self):
		del self._DlvryIntrvl
		self._DlvryIntrvl = base_types.UninitialisedField(self, 'DlvryIntrvl', TimePeriodDetails1, True)

	@property
	def Drtn(self):
		return self._Drtn

	@Drtn.setter
	def Drtn(self, value):
		self._Drtn = value if value is not None else base_types.UninitialisedField(self, 'Drtn', DurationType1Code, False)

	@Drtn.deleter
	def Drtn(self):
		del self._Drtn
		self._Drtn = base_types.UninitialisedField(self, 'Drtn', DurationType1Code, False)

	@property
	def PricTmIntrvlQty(self):
		return self._PricTmIntrvlQty

	@PricTmIntrvlQty.setter
	def PricTmIntrvlQty(self, value):
		self._PricTmIntrvlQty = value if value is not None else base_types.UninitialisedField(self, 'PricTmIntrvlQty', AmountAndDirection106, False)

	@PricTmIntrvlQty.deleter
	def PricTmIntrvlQty(self):
		del self._PricTmIntrvlQty
		self._PricTmIntrvlQty = base_types.UninitialisedField(self, 'PricTmIntrvlQty', AmountAndDirection106, False)

	@property
	def QtyUnit(self):
		return self._QtyUnit

	@QtyUnit.setter
	def QtyUnit(self, value):
		self._QtyUnit = value if value is not None else base_types.UninitialisedField(self, 'QtyUnit', EnergyQuantityUnit2Choice, False)

	@QtyUnit.deleter
	def QtyUnit(self):
		del self._QtyUnit
		self._QtyUnit = base_types.UninitialisedField(self, 'QtyUnit', EnergyQuantityUnit2Choice, False)

	@property
	def WkDay(self):
		return self._WkDay

	@WkDay.setter
	def WkDay(self, value):
		self._WkDay = value if value is not None else base_types.UninitialisedField(self, 'WkDay', WeekDay3Code, True)

	@WkDay.deleter
	def WkDay(self):
		del self._WkDay
		self._WkDay = base_types.UninitialisedField(self, 'WkDay', WeekDay3Code, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DlvryCpcty', type=Quantity47Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryDt', type=DatePeriod1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryIntrvl', type=TimePeriodDetails1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Drtn', type=DurationType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTmIntrvlQty', type=AmountAndDirection106, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QtyUnit', type=EnergyQuantityUnit2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WkDay', type=WeekDay3Code, min=0, max=None, mutex_group=None, array=True),
	))