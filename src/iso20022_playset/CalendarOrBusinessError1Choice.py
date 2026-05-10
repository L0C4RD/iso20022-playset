import base_types
import CalendarData1
import ErrorHandling4

class CalendarOrBusinessError1Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_CalData"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	@property
	def CalData(self):
		return self._CalData

	@CalData.setter
	def CalData(self, value):
		self._CalData = value if type(value) != auto else self.make_default("CalData")

	@CalData.deleter
	def CalData(self):
		del self._CalData
		self._CalData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='CalData', type=CalendarData1, min=1, max=None, mutex_group=1, array=True),
	))

