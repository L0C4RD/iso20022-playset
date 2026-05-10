from . import base_types
from .AmountAndDirection106 import AmountAndDirection106
from .ISODate import ISODate

class Schedule11(base_types._BaseFieldType):

	__slots__ = ["_UadjstdFctvDt", "_UadjstdEndDt", "_Amt"]
	@property
	def UadjstdFctvDt(self):
		return self._UadjstdFctvDt

	@UadjstdFctvDt.setter
	def UadjstdFctvDt(self, value):
		self._UadjstdFctvDt = value if type(value) != base_types.auto else self.make_default("UadjstdFctvDt")

	@UadjstdFctvDt.deleter
	def UadjstdFctvDt(self):
		del self._UadjstdFctvDt
		self._UadjstdFctvDt = None

	@property
	def UadjstdEndDt(self):
		return self._UadjstdEndDt

	@UadjstdEndDt.setter
	def UadjstdEndDt(self, value):
		self._UadjstdEndDt = value if type(value) != base_types.auto else self.make_default("UadjstdEndDt")

	@UadjstdEndDt.deleter
	def UadjstdEndDt(self):
		del self._UadjstdEndDt
		self._UadjstdEndDt = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UadjstdFctvDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UadjstdEndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountAndDirection106, min=1, max=1, mutex_group=None, array=False),
	))

