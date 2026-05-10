from . import base_types
from ._BusinessDay9 import BusinessDay9
from ._ErrorHandling5 import ErrorHandling5

class BusinessDayReportOrError10Choice(base_types._BaseFieldType):

	__slots__ = ["_BizDayInf", "_BizErr"]
	@property
	def BizDayInf(self):
		return self._BizDayInf

	@BizDayInf.setter
	def BizDayInf(self, value):
		self._BizDayInf = value if type(value) != base_types.auto else self.make_default("BizDayInf")

	@BizDayInf.deleter
	def BizDayInf(self):
		del self._BizDayInf
		self._BizDayInf = None

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
		base_types.FieldEntry(name='BizDayInf', type=BusinessDay9, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

