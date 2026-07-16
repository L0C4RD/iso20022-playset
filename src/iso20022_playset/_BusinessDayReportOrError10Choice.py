# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessDay9
from . import ErrorHandling5

class BusinessDayReportOrError10Choice(base_types._BaseFieldType):

	__slots__ = ["_BizDayInf", "_BizErr"]
	@property
	def BizDayInf(self):
		return self._BizDayInf

	@BizDayInf.setter
	def BizDayInf(self, value):
		self._BizDayInf = value if value is not None else base_types.UninitialisedField(self, 'BizDayInf', BusinessDay9, False)

	@BizDayInf.deleter
	def BizDayInf(self):
		del self._BizDayInf
		self._BizDayInf = base_types.UninitialisedField(self, 'BizDayInf', BusinessDay9, False)

	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizDayInf', type=BusinessDay9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))