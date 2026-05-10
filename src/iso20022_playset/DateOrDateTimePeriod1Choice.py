from . import base_types
from .DateTimePeriod1 import DateTimePeriod1
from .DatePeriod2 import DatePeriod2

class DateOrDateTimePeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_DtTm", "_Dt"]
	@property
	def DtTm(self):
		return self._DtTm

	@DtTm.setter
	def DtTm(self, value):
		self._DtTm = value if type(value) != base_types.auto else self.make_default("DtTm")

	@DtTm.deleter
	def DtTm(self):
		del self._DtTm
		self._DtTm = None

	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=DatePeriod2, min=0, max=1, mutex_group=1, array=False),
	))

