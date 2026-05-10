from . import base_types
from .DateTimePeriod1Choice import DateTimePeriod1Choice
from .DatePeriodSearch1Choice import DatePeriodSearch1Choice

class DateAndDateTimeSearch3Choice(base_types._BaseFieldType):

	__slots__ = ["_DtSch", "_DtTmSch"]
	@property
	def DtSch(self):
		return self._DtSch

	@DtSch.setter
	def DtSch(self, value):
		self._DtSch = value if type(value) != auto else self.make_default("DtSch")

	@DtSch.deleter
	def DtSch(self):
		del self._DtSch
		self._DtSch = None

	@property
	def DtTmSch(self):
		return self._DtTmSch

	@DtTmSch.setter
	def DtTmSch(self, value):
		self._DtTmSch = value if type(value) != auto else self.make_default("DtTmSch")

	@DtTmSch.deleter
	def DtTmSch(self):
		del self._DtTmSch
		self._DtTmSch = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtSch', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtTmSch', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=1, array=False),
	))

