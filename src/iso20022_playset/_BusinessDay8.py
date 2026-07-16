# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessDayReportOrError10Choice
from . import SystemIdentification2Choice

class BusinessDay8(base_types._BaseFieldType):

	__slots__ = ["_BizDayOrErr", "_SysId"]
	@property
	def BizDayOrErr(self):
		return self._BizDayOrErr

	@BizDayOrErr.setter
	def BizDayOrErr(self, value):
		self._BizDayOrErr = value if value is not None else base_types.UninitialisedField(self, 'BizDayOrErr', BusinessDayReportOrError10Choice, False)

	@BizDayOrErr.deleter
	def BizDayOrErr(self):
		del self._BizDayOrErr
		self._BizDayOrErr = base_types.UninitialisedField(self, 'BizDayOrErr', BusinessDayReportOrError10Choice, False)

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if value is not None else base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, True)

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = base_types.UninitialisedField(self, 'SysId', SystemIdentification2Choice, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizDayOrErr', type=BusinessDayReportOrError10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=1, max=None, mutex_group=None, array=True),
	))