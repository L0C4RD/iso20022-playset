from . import base_types
import ErrorHandling5
import BusinessDay8

class BusinessDayReportOrError9Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_BizRpt"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	@property
	def BizRpt(self):
		return self._BizRpt

	@BizRpt.setter
	def BizRpt(self, value):
		self._BizRpt = value if type(value) != auto else self.make_default("BizRpt")

	@BizRpt.deleter
	def BizRpt(self):
		del self._BizRpt
		self._BizRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='BizRpt', type=BusinessDay8, min=1, max=None, mutex_group=1, array=True),
	))

