import base_types
import ErrorHandling5
import SecurityOrBusinessError4Choice

class SecurityOrOperationalError4Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_SctyRptOrBizErr"]
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
	def SctyRptOrBizErr(self):
		return self._SctyRptOrBizErr

	@SctyRptOrBizErr.setter
	def SctyRptOrBizErr(self, value):
		self._SctyRptOrBizErr = value if type(value) != auto else self.make_default("SctyRptOrBizErr")

	@SctyRptOrBizErr.deleter
	def SctyRptOrBizErr(self):
		del self._SctyRptOrBizErr
		self._SctyRptOrBizErr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctyRptOrBizErr', type=SecurityOrBusinessError4Choice, min=0, max=1, mutex_group=1, array=False),
	))

