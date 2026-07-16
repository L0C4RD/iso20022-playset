# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DayOfMonthNumber
from . import Frequency14Code
from . import WeekDay3Code

class TradeQueryExecutionFrequency3(base_types._BaseFieldType):

	__slots__ = ["_DayOfMnth", "_DlvryDay", "_FrqcyTp"]
	@property
	def DayOfMnth(self):
		return self._DayOfMnth

	@DayOfMnth.setter
	def DayOfMnth(self, value):
		self._DayOfMnth = value if value is not None else base_types.UninitialisedField(self, 'DayOfMnth', DayOfMonthNumber, True)

	@DayOfMnth.deleter
	def DayOfMnth(self):
		del self._DayOfMnth
		self._DayOfMnth = base_types.UninitialisedField(self, 'DayOfMnth', DayOfMonthNumber, True)

	@property
	def DlvryDay(self):
		return self._DlvryDay

	@DlvryDay.setter
	def DlvryDay(self, value):
		self._DlvryDay = value if value is not None else base_types.UninitialisedField(self, 'DlvryDay', WeekDay3Code, True)

	@DlvryDay.deleter
	def DlvryDay(self):
		del self._DlvryDay
		self._DlvryDay = base_types.UninitialisedField(self, 'DlvryDay', WeekDay3Code, True)

	@property
	def FrqcyTp(self):
		return self._FrqcyTp

	@FrqcyTp.setter
	def FrqcyTp(self, value):
		self._FrqcyTp = value if value is not None else base_types.UninitialisedField(self, 'FrqcyTp', Frequency14Code, False)

	@FrqcyTp.deleter
	def FrqcyTp(self):
		del self._FrqcyTp
		self._FrqcyTp = base_types.UninitialisedField(self, 'FrqcyTp', Frequency14Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DayOfMnth', type=DayOfMonthNumber, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DlvryDay', type=WeekDay3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrqcyTp', type=Frequency14Code, min=1, max=1, mutex_group=None, array=False),
	))