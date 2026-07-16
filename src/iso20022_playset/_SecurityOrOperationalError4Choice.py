# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import SecurityOrBusinessError4Choice

class SecurityOrOperationalError4Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_SctyRptOrBizErr"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if value is not None else base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = base_types.UninitialisedField(self, 'OprlErr', ErrorHandling5, True)

	@property
	def SctyRptOrBizErr(self):
		return self._SctyRptOrBizErr

	@SctyRptOrBizErr.setter
	def SctyRptOrBizErr(self, value):
		self._SctyRptOrBizErr = value if value is not None else base_types.UninitialisedField(self, 'SctyRptOrBizErr', SecurityOrBusinessError4Choice, False)

	@SctyRptOrBizErr.deleter
	def SctyRptOrBizErr(self):
		del self._SctyRptOrBizErr
		self._SctyRptOrBizErr = base_types.UninitialisedField(self, 'SctyRptOrBizErr', SecurityOrBusinessError4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctyRptOrBizErr', type=SecurityOrBusinessError4Choice, min=0, max=1, mutex_group=1, array=False),
	))