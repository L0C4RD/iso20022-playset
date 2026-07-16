# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareAmountAndDirection3
from . import CompareDatePeriod2
from . import CompareDurationType1
from . import CompareEnergyQuantityUnit1
from . import CompareLongFraction19DecimalNumber1
from . import CompareTimePeriod2
from . import CompareWeekDay1

class CompareEnergyDeliveryAttribute1(base_types._BaseFieldType):

	__slots__ = ["_NrgyDlvryCpcty", "_NrgyDlvryIntrvl", "_NrgyDrtn", "_NrgyDt", "_NrgyPricTmIntrvlQty", "_NrgyQtyUnit", "_NrgyWkDay"]
	@property
	def NrgyDlvryCpcty(self):
		return self._NrgyDlvryCpcty

	@NrgyDlvryCpcty.setter
	def NrgyDlvryCpcty(self, value):
		self._NrgyDlvryCpcty = value if value is not None else base_types.UninitialisedField(self, 'NrgyDlvryCpcty', CompareLongFraction19DecimalNumber1, False)

	@NrgyDlvryCpcty.deleter
	def NrgyDlvryCpcty(self):
		del self._NrgyDlvryCpcty
		self._NrgyDlvryCpcty = base_types.UninitialisedField(self, 'NrgyDlvryCpcty', CompareLongFraction19DecimalNumber1, False)

	@property
	def NrgyDlvryIntrvl(self):
		return self._NrgyDlvryIntrvl

	@NrgyDlvryIntrvl.setter
	def NrgyDlvryIntrvl(self, value):
		self._NrgyDlvryIntrvl = value if value is not None else base_types.UninitialisedField(self, 'NrgyDlvryIntrvl', CompareTimePeriod2, True)

	@NrgyDlvryIntrvl.deleter
	def NrgyDlvryIntrvl(self):
		del self._NrgyDlvryIntrvl
		self._NrgyDlvryIntrvl = base_types.UninitialisedField(self, 'NrgyDlvryIntrvl', CompareTimePeriod2, True)

	@property
	def NrgyDrtn(self):
		return self._NrgyDrtn

	@NrgyDrtn.setter
	def NrgyDrtn(self, value):
		self._NrgyDrtn = value if value is not None else base_types.UninitialisedField(self, 'NrgyDrtn', CompareDurationType1, False)

	@NrgyDrtn.deleter
	def NrgyDrtn(self):
		del self._NrgyDrtn
		self._NrgyDrtn = base_types.UninitialisedField(self, 'NrgyDrtn', CompareDurationType1, False)

	@property
	def NrgyDt(self):
		return self._NrgyDt

	@NrgyDt.setter
	def NrgyDt(self, value):
		self._NrgyDt = value if value is not None else base_types.UninitialisedField(self, 'NrgyDt', CompareDatePeriod2, False)

	@NrgyDt.deleter
	def NrgyDt(self):
		del self._NrgyDt
		self._NrgyDt = base_types.UninitialisedField(self, 'NrgyDt', CompareDatePeriod2, False)

	@property
	def NrgyPricTmIntrvlQty(self):
		return self._NrgyPricTmIntrvlQty

	@NrgyPricTmIntrvlQty.setter
	def NrgyPricTmIntrvlQty(self, value):
		self._NrgyPricTmIntrvlQty = value if value is not None else base_types.UninitialisedField(self, 'NrgyPricTmIntrvlQty', CompareAmountAndDirection3, False)

	@NrgyPricTmIntrvlQty.deleter
	def NrgyPricTmIntrvlQty(self):
		del self._NrgyPricTmIntrvlQty
		self._NrgyPricTmIntrvlQty = base_types.UninitialisedField(self, 'NrgyPricTmIntrvlQty', CompareAmountAndDirection3, False)

	@property
	def NrgyQtyUnit(self):
		return self._NrgyQtyUnit

	@NrgyQtyUnit.setter
	def NrgyQtyUnit(self, value):
		self._NrgyQtyUnit = value if value is not None else base_types.UninitialisedField(self, 'NrgyQtyUnit', CompareEnergyQuantityUnit1, False)

	@NrgyQtyUnit.deleter
	def NrgyQtyUnit(self):
		del self._NrgyQtyUnit
		self._NrgyQtyUnit = base_types.UninitialisedField(self, 'NrgyQtyUnit', CompareEnergyQuantityUnit1, False)

	@property
	def NrgyWkDay(self):
		return self._NrgyWkDay

	@NrgyWkDay.setter
	def NrgyWkDay(self, value):
		self._NrgyWkDay = value if value is not None else base_types.UninitialisedField(self, 'NrgyWkDay', CompareWeekDay1, True)

	@NrgyWkDay.deleter
	def NrgyWkDay(self):
		del self._NrgyWkDay
		self._NrgyWkDay = base_types.UninitialisedField(self, 'NrgyWkDay', CompareWeekDay1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NrgyDlvryCpcty', type=CompareLongFraction19DecimalNumber1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyDlvryIntrvl', type=CompareTimePeriod2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NrgyDrtn', type=CompareDurationType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyDt', type=CompareDatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyPricTmIntrvlQty', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyQtyUnit', type=CompareEnergyQuantityUnit1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrgyWkDay', type=CompareWeekDay1, min=0, max=None, mutex_group=None, array=True),
	))