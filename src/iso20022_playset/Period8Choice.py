from . import base_types
from .DateTimePeriod1 import DateTimePeriod1
from .ISODateTime import ISODateTime

class Period8Choice(base_types._BaseFieldType):

	__slots__ = ["_FrDtToDt", "_DtTm", "_FrDtTm", "_ToDtTm"]
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
	def FrDtTm(self):
		return self._FrDtTm

	@FrDtTm.setter
	def FrDtTm(self, value):
		self._FrDtTm = value if type(value) != base_types.auto else self.make_default("FrDtTm")

	@FrDtTm.deleter
	def FrDtTm(self):
		del self._FrDtTm
		self._FrDtTm = None

	@property
	def ToDtTm(self):
		return self._ToDtTm

	@ToDtTm.setter
	def ToDtTm(self, value):
		self._ToDtTm = value if type(value) != base_types.auto else self.make_default("ToDtTm")

	@ToDtTm.deleter
	def ToDtTm(self):
		del self._ToDtTm
		self._ToDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDtToDt', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
	))

