# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import SecuritiesAuditTrailReport4

class SecuritiesAuditTrailOrOperationalError4Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_SctiesAudtTrlRpt"]
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
	def SctiesAudtTrlRpt(self):
		return self._SctiesAudtTrlRpt

	@SctiesAudtTrlRpt.setter
	def SctiesAudtTrlRpt(self, value):
		self._SctiesAudtTrlRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesAudtTrlRpt', SecuritiesAuditTrailReport4, True)

	@SctiesAudtTrlRpt.deleter
	def SctiesAudtTrlRpt(self):
		del self._SctiesAudtTrlRpt
		self._SctiesAudtTrlRpt = base_types.UninitialisedField(self, 'SctiesAudtTrlRpt', SecuritiesAuditTrailReport4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctiesAudtTrlRpt', type=SecuritiesAuditTrailReport4, min=1, max=None, mutex_group=1, array=True),
	))