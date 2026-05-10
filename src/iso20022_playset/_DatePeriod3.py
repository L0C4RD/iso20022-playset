from . import base_types
from ._ISODate import ISODate

class DatePeriod3(base_types._BaseFieldType):

	__slots__ = ["_ToDt", "_FrDt"]
	@property
	def FrDt(self):
		return self._FrDt

	@FrDt.setter
	def FrDt(self, value):
		self._FrDt = value if type(value) != base_types.auto else self.make_default("FrDt")

	@FrDt.deleter
	def FrDt(self):
		del self._FrDt
		self._FrDt = None

	@property
	def ToDt(self):
		return self._ToDt

	@ToDt.setter
	def ToDt(self, value):
		self._ToDt = value if type(value) != base_types.auto else self.make_default("ToDt")

	@ToDt.deleter
	def ToDt(self):
		del self._ToDt
		self._ToDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

