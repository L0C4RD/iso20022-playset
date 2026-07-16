# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DatePeriod2
from . import ISODate
from . import TaxRecordPeriod1Code

class TaxPeriod2(base_types._BaseFieldType):

	__slots__ = ["_FrToDt", "_Tp", "_Yr"]
	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if value is not None else base_types.UninitialisedField(self, 'FrToDt', DatePeriod2, False)

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = base_types.UninitialisedField(self, 'FrToDt', DatePeriod2, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', TaxRecordPeriod1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', TaxRecordPeriod1Code, False)

	@property
	def Yr(self):
		return self._Yr

	@Yr.setter
	def Yr(self, value):
		self._Yr = value if value is not None else base_types.UninitialisedField(self, 'Yr', ISODate, False)

	@Yr.deleter
	def Yr(self):
		del self._Yr
		self._Yr = base_types.UninitialisedField(self, 'Yr', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrToDt', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxRecordPeriod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))