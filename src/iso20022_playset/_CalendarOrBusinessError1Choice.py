from . import base_types
from ._ErrorHandling4 import ErrorHandling4
from ._CalendarData1 import CalendarData1

class CalendarOrBusinessError1Choice(base_types._BaseFieldType):

	__slots__ = ["_CalData", "_BizErr"]
	@property
	def CalData(self):
		return self._CalData

	@CalData.setter
	def CalData(self, value):
		self._CalData = value if type(value) != base_types.auto else self.make_default("CalData")

	@CalData.deleter
	def CalData(self):
		del self._CalData
		self._CalData = None

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != base_types.auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CalData', type=CalendarData1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling4, min=1, max=None, mutex_group=1, array=True),
	))

