from . import base_types
from .ISOTime import ISOTime

class TimePeriodDetails1(base_types._BaseFieldType):

	__slots__ = ["_ToTm", "_FrTm"]
	@property
	def ToTm(self):
		return self._ToTm

	@ToTm.setter
	def ToTm(self, value):
		self._ToTm = value if type(value) != base_types.auto else self.make_default("ToTm")

	@ToTm.deleter
	def ToTm(self):
		del self._ToTm
		self._ToTm = None

	@property
	def FrTm(self):
		return self._FrTm

	@FrTm.setter
	def FrTm(self, value):
		self._FrTm = value if type(value) != base_types.auto else self.make_default("FrTm")

	@FrTm.deleter
	def FrTm(self):
		del self._FrTm
		self._FrTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ToTm', type=ISOTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrTm', type=ISOTime, min=1, max=1, mutex_group=None, array=False),
	))

