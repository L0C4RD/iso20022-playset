import base_types
import Period2
import ISOYearMonth
import ISODate

class DatePeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_FrDtToDt", "_Dt", "_DtMnth"]
	@property
	def FrDtToDt(self):
		return self._FrDtToDt

	@FrDtToDt.setter
	def FrDtToDt(self, value):
		self._FrDtToDt = value if type(value) != auto else self.make_default("FrDtToDt")

	@FrDtToDt.deleter
	def FrDtToDt(self):
		del self._FrDtToDt
		self._FrDtToDt = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def DtMnth(self):
		return self._DtMnth

	@DtMnth.setter
	def DtMnth(self, value):
		self._DtMnth = value if type(value) != auto else self.make_default("DtMnth")

	@DtMnth.deleter
	def DtMnth(self):
		del self._DtMnth
		self._DtMnth = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDtToDt', type=Period2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtMnth', type=ISOYearMonth, min=0, max=1, mutex_group=1, array=False),
	))

