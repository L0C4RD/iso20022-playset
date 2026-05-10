from . import base_types
from .Number import Number
from .ISODateTime import ISODateTime

class LocalDateTime1(base_types._BaseFieldType):

	__slots__ = ["_FrDtTm", "_UTCOffset", "_ToDtTm"]
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
	def UTCOffset(self):
		return self._UTCOffset

	@UTCOffset.setter
	def UTCOffset(self, value):
		self._UTCOffset = value if type(value) != base_types.auto else self.make_default("UTCOffset")

	@UTCOffset.deleter
	def UTCOffset(self):
		del self._UTCOffset
		self._UTCOffset = None

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
		base_types.FieldEntry(name='FrDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UTCOffset', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ToDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))

