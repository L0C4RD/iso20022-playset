from . import base_types
import DatePeriod2
import ISOYear
import TaxRecordPeriod1Code

class TaxPeriod3(base_types._BaseFieldType):

	__slots__ = ["_FrToDt", "_Tp", "_Yr"]
	@property
	def FrToDt(self):
		return self._FrToDt

	@FrToDt.setter
	def FrToDt(self, value):
		self._FrToDt = value if type(value) != auto else self.make_default("FrToDt")

	@FrToDt.deleter
	def FrToDt(self):
		del self._FrToDt
		self._FrToDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Yr(self):
		return self._Yr

	@Yr.setter
	def Yr(self, value):
		self._Yr = value if type(value) != auto else self.make_default("Yr")

	@Yr.deleter
	def Yr(self):
		del self._Yr
		self._Yr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrToDt', type=DatePeriod2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=TaxRecordPeriod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yr', type=ISOYear, min=0, max=1, mutex_group=None, array=False),
	))

