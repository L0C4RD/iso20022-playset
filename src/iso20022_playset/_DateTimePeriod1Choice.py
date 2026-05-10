from . import base_types
from ._DateTimePeriod1 import DateTimePeriod1
from ._ISODateTime import ISODateTime

class DateTimePeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_DtTmRg", "_ToDtTm", "_FrDtTm"]
	@property
	def DtTmRg(self):
		return self._DtTmRg

	@DtTmRg.setter
	def DtTmRg(self, value):
		self._DtTmRg = value if type(value) != base_types.auto else self.make_default("DtTmRg")

	@DtTmRg.deleter
	def DtTmRg(self):
		del self._DtTmRg
		self._DtTmRg = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtTmRg', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=0, max=1, mutex_group=1, array=False),
	))

