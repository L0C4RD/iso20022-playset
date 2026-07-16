# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISOYearMonth
from . import Period2

class DatePeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_DtMnth", "_FrDtToDt"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if value is not None else base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = base_types.UninitialisedField(self, 'Dt', ISODate, False)

	@property
	def DtMnth(self):
		return self._DtMnth

	@DtMnth.setter
	def DtMnth(self, value):
		self._DtMnth = value if value is not None else base_types.UninitialisedField(self, 'DtMnth', ISOYearMonth, False)

	@DtMnth.deleter
	def DtMnth(self):
		del self._DtMnth
		self._DtMnth = base_types.UninitialisedField(self, 'DtMnth', ISOYearMonth, False)

	@property
	def FrDtToDt(self):
		return self._FrDtToDt

	@FrDtToDt.setter
	def FrDtToDt(self, value):
		self._FrDtToDt = value if value is not None else base_types.UninitialisedField(self, 'FrDtToDt', Period2, False)

	@FrDtToDt.deleter
	def FrDtToDt(self):
		del self._FrDtToDt
		self._FrDtToDt = base_types.UninitialisedField(self, 'FrDtToDt', Period2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtMnth', type=ISOYearMonth, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtToDt', type=Period2, min=0, max=1, mutex_group=1, array=False),
	))