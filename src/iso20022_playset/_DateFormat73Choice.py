from . import base_types
from ._DateType8Code import DateType8Code
from ._ISODate import ISODate

class DateFormat73Choice(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_NotSpcfdDt"]
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

	@property
	def NotSpcfdDt(self):
		return self._NotSpcfdDt

	@NotSpcfdDt.setter
	def NotSpcfdDt(self, value):
		self._NotSpcfdDt = value if type(value) != base_types.auto else self.make_default("NotSpcfdDt")

	@NotSpcfdDt.deleter
	def NotSpcfdDt(self):
		del self._NotSpcfdDt
		self._NotSpcfdDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NotSpcfdDt', type=DateType8Code, min=0, max=1, mutex_group=1, array=False),
	))

