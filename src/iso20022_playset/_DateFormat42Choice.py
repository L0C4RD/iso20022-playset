# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISOYearMonth

class DateFormat42Choice(base_types._BaseFieldType):

	__slots__ = ["_YrMnth", "_YrMnthDay"]
	@property
	def YrMnth(self):
		return self._YrMnth

	@YrMnth.setter
	def YrMnth(self, value):
		self._YrMnth = value if value is not None else base_types.UninitialisedField(self, 'YrMnth', ISOYearMonth, False)

	@YrMnth.deleter
	def YrMnth(self):
		del self._YrMnth
		self._YrMnth = base_types.UninitialisedField(self, 'YrMnth', ISOYearMonth, False)

	@property
	def YrMnthDay(self):
		return self._YrMnthDay

	@YrMnthDay.setter
	def YrMnthDay(self, value):
		self._YrMnthDay = value if value is not None else base_types.UninitialisedField(self, 'YrMnthDay', ISODate, False)

	@YrMnthDay.deleter
	def YrMnthDay(self):
		del self._YrMnthDay
		self._YrMnthDay = base_types.UninitialisedField(self, 'YrMnthDay', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='YrMnth', type=ISOYearMonth, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='YrMnthDay', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))