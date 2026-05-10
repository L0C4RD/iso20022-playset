from . import base_types
from ._ISODate import ISODate
from ._Period2 import Period2

class Period4Choice(base_types._BaseFieldType):

	__slots__ = ["_ToDt", "_FrDtToDt", "_Dt", "_FrDt"]
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

	@property
	def FrDtToDt(self):
		return self._FrDtToDt

	@FrDtToDt.setter
	def FrDtToDt(self, value):
		self._FrDtToDt = value if type(value) != base_types.auto else self.make_default("FrDtToDt")

	@FrDtToDt.deleter
	def FrDtToDt(self):
		del self._FrDtToDt
		self._FrDtToDt = None

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
	def FrDt(self):
		return self._FrDt

	@FrDt.setter
	def FrDt(self, value):
		self._FrDt = value if type(value) != base_types.auto else self.make_default("FrDt")

	@FrDt.deleter
	def FrDt(self):
		del self._FrDt
		self._FrDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ToDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtToDt', type=Period2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Dt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))

