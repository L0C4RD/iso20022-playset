# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriodSearch1Choice
from . import DateTimeSearch2Choice

class DateAndDateTimeSearch4Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_DtTm"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', DatePeriodSearch1Choice, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', DatePeriodSearch1Choice, False)

	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if value is not None else base_types.UninitialisedField(self, 'DtTm', DateTimeSearch2Choice, False)

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = base_types.UninitialisedField(self, 'DtTm', DateTimeSearch2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=DatePeriodSearch1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtTm', type=DateTimeSearch2Choice, min=0, max=1, mutex_group=1, array=False),
	))