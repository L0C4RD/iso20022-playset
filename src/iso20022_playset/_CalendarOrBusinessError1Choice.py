# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CalendarData1
from . import ErrorHandling4

class CalendarOrBusinessError1Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_CalData"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling4, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling4, True)

	@property
	def CalData(self):
		return self._CalData

	@CalData.setter
	def CalData(self, value):
		self._CalData = value if value is not None else base_types.UninitialisedField(self, 'CalData', CalendarData1, True)

	@CalData.deleter
	def CalData(self):
		del self._CalData
		self._CalData = base_types.UninitialisedField(self, 'CalData', CalendarData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='CalData', type=CalendarData1, min=1, max=None, mutex_group=1, array=True),
	))