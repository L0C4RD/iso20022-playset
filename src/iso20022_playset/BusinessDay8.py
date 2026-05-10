from . import base_types
from .BusinessDayReportOrError10Choice import BusinessDayReportOrError10Choice
from .SystemIdentification2Choice import SystemIdentification2Choice

class BusinessDay8(base_types._BaseFieldType):

	__slots__ = ["_BizDayOrErr", "_SysId"]
	@property
	def BizDayOrErr(self):
		return self._BizDayOrErr

	@BizDayOrErr.setter
	def BizDayOrErr(self, value):
		self._BizDayOrErr = value if type(value) != base_types.auto else self.make_default("BizDayOrErr")

	@BizDayOrErr.deleter
	def BizDayOrErr(self):
		del self._BizDayOrErr
		self._BizDayOrErr = None

	@property
	def SysId(self):
		return self._SysId

	@SysId.setter
	def SysId(self, value):
		self._SysId = value if type(value) != base_types.auto else self.make_default("SysId")

	@SysId.deleter
	def SysId(self):
		del self._SysId
		self._SysId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizDayOrErr', type=BusinessDayReportOrError10Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysId', type=SystemIdentification2Choice, min=1, max=None, mutex_group=None, array=True),
	))

