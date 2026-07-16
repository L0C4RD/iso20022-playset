# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CalendarReport1
from . import ErrorHandling4

class CalendarReportOrError1Choice(base_types._BaseFieldType):

	__slots__ = ["_CalRpt", "_OprlErr"]
	@property
	def CalRpt(self):
		return self._CalRpt

	@CalRpt.setter
	def CalRpt(self, value):
		self._CalRpt = value if value is not None else base_types.UninitialisedField(self, 'CalRpt', CalendarReport1, False)

	@CalRpt.deleter
	def CalRpt(self):
		del self._CalRpt
		self._CalRpt = base_types.UninitialisedField(self, 'CalRpt', CalendarReport1, False)

	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if value is not None else base_types.UninitialisedField(self, 'OprlErr', ErrorHandling4, True)

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = base_types.UninitialisedField(self, 'OprlErr', ErrorHandling4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CalRpt', type=CalendarReport1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling4, min=1, max=None, mutex_group=1, array=True),
	))