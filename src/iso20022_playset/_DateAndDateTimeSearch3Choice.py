# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriodSearch1Choice
from . import DateTimePeriod1Choice

class DateAndDateTimeSearch3Choice(base_types._BaseFieldType):

	__slots__ = ["_DtSch", "_DtTmSch"]
	@property
	def DtSch(self):
		return self._DtSch

	@DtSch.setter
	def DtSch(self, value):
		self._DtSch = value if value is not None else base_types.UninitialisedField(self, 'DtSch', DatePeriodSearch1Choice, False)

	@DtSch.deleter
	def DtSch(self):
		del self._DtSch
		self._DtSch = base_types.UninitialisedField(self, 'DtSch', DatePeriodSearch1Choice, False)

	@property
	def DtTmSch(self):
		return self._DtTmSch

	@DtTmSch.setter
	def DtTmSch(self, value):
		self._DtTmSch = value if value is not None else base_types.UninitialisedField(self, 'DtTmSch', DateTimePeriod1Choice, False)

	@DtTmSch.deleter
	def DtTmSch(self):
		del self._DtTmSch
		self._DtTmSch = base_types.UninitialisedField(self, 'DtTmSch', DateTimePeriod1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtSch', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtTmSch', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=1, array=False),
	))