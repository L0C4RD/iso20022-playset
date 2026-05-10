from . import base_types
from ._CalendarReport1 import CalendarReport1
from ._ErrorHandling4 import ErrorHandling4

class CalendarReportOrError1Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_CalRpt"]
	@property
	def CalRpt(self):
		return self._CalRpt

	@CalRpt.setter
	def CalRpt(self, value):
		self._CalRpt = value if type(value) != base_types.auto else self.make_default("CalRpt")

	@CalRpt.deleter
	def CalRpt(self):
		del self._CalRpt
		self._CalRpt = None

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CalRpt', type=CalendarReport1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling4, min=1, max=None, mutex_group=1, array=True),
	))

