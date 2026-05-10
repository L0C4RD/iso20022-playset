from . import base_types
from ._Frequency14Code import Frequency14Code
from ._DayOfMonthNumber import DayOfMonthNumber
from ._WeekDay3Code import WeekDay3Code

class TradeQueryExecutionFrequency3(base_types._BaseFieldType):

	__slots__ = ["_DayOfMnth", "_DlvryDay", "_FrqcyTp"]
	@property
	def DayOfMnth(self):
		return self._DayOfMnth

	@DayOfMnth.setter
	def DayOfMnth(self, value):
		self._DayOfMnth = value if type(value) != base_types.auto else self.make_default("DayOfMnth")

	@DayOfMnth.deleter
	def DayOfMnth(self):
		del self._DayOfMnth
		self._DayOfMnth = None

	@property
	def DlvryDay(self):
		return self._DlvryDay

	@DlvryDay.setter
	def DlvryDay(self, value):
		self._DlvryDay = value if type(value) != base_types.auto else self.make_default("DlvryDay")

	@DlvryDay.deleter
	def DlvryDay(self):
		del self._DlvryDay
		self._DlvryDay = None

	@property
	def FrqcyTp(self):
		return self._FrqcyTp

	@FrqcyTp.setter
	def FrqcyTp(self, value):
		self._FrqcyTp = value if type(value) != base_types.auto else self.make_default("FrqcyTp")

	@FrqcyTp.deleter
	def FrqcyTp(self):
		del self._FrqcyTp
		self._FrqcyTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayOfMnth', type=DayOfMonthNumber, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryDay', type=WeekDay3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrqcyTp', type=Frequency14Code, min=1, max=1, mutex_group=None, array=False),
	))

