import base_types
import ISOYearMonth
import ISODate

class DateFormat42Choice(base_types._BaseFieldType):

	__slots__ = ["_YrMnth", "_YrMnthDay"]
	@property
	def YrMnth(self):
		return self._YrMnth

	@YrMnth.setter
	def YrMnth(self, value):
		self._YrMnth = value if type(value) != auto else self.make_default("YrMnth")

	@YrMnth.deleter
	def YrMnth(self):
		del self._YrMnth
		self._YrMnth = None

	@property
	def YrMnthDay(self):
		return self._YrMnthDay

	@YrMnthDay.setter
	def YrMnthDay(self, value):
		self._YrMnthDay = value if type(value) != auto else self.make_default("YrMnthDay")

	@YrMnthDay.deleter
	def YrMnthDay(self):
		del self._YrMnthDay
		self._YrMnthDay = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='YrMnth', type=ISOYearMonth, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='YrMnthDay', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))

