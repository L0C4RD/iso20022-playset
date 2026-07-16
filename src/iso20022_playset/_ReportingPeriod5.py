# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod3
from . import QueryType3Code
from . import TimePeriodDetails1

class ReportingPeriod5(base_types._BaseFieldType):

	__slots__ = ["_FrToDt", "_FrToTm", "_Tp"]
	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if value is not None else base_types.UninitialisedField(self, 'FrToDt', DatePeriod3, False)

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = base_types.UninitialisedField(self, 'FrToDt', DatePeriod3, False)

	@property
	def FrToTm(self):
		return self._FrToTm

	@FrToTm.setter
	def FrToTm(self, value):
		self._FrToTm = value if value is not None else base_types.UninitialisedField(self, 'FrToTm', TimePeriodDetails1, False)

	@FrToTm.deleter
	def FrToTm(self):
		del self._FrToTm
		self._FrToTm = base_types.UninitialisedField(self, 'FrToTm', TimePeriodDetails1, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', QueryType3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', QueryType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrToDt', type=DatePeriod3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrToTm', type=TimePeriodDetails1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=QueryType3Code, min=1, max=1, mutex_group=None, array=False),
	))