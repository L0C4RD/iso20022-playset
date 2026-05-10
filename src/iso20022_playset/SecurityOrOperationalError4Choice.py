import base_types
import SecurityOrBusinessError4Choice
import ErrorHandling5

class SecurityOrOperationalError4Choice(base_types._BaseFieldType):

	__slots__ = ["_SctyRptOrBizErr", "_OprlErr"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='SctyRptOrBizErr', type=SecurityOrBusinessError4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

