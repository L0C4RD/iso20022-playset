from . import base_types
import Period2
import DateTimePeriod1

class Period7Choice(base_types._BaseFieldType):

	__slots__ = ["_FrDtTmToDtTm", "_FrDtToDt"]
	@property
	def FrDtTmToDtTm(self):
		return self._FrDtTmToDtTm

	@FrDtTmToDtTm.setter
	def FrDtTmToDtTm(self, value):
		self._FrDtTmToDtTm = value if type(value) != auto else self.make_default("FrDtTmToDtTm")

	@FrDtTmToDtTm.deleter
	def FrDtTmToDtTm(self):
		del self._FrDtTmToDtTm
		self._FrDtTmToDtTm = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrDtTmToDtTm', type=DateTimePeriod1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='FrDtToDt', type=Period2, min=0, max=1, mutex_group=1, array=False),
	))

