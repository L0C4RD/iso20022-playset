# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import SecuritiesAccountAuditTrailReport3

class SecuritiesAccountAuditTrailOrOperationalError3Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_SctiesAcctAudtTrlRpt"]
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
	def SctiesAcctAudtTrlRpt(self):
		return self._SctiesAcctAudtTrlRpt

	@SctiesAcctAudtTrlRpt.setter
	def SctiesAcctAudtTrlRpt(self, value):
		self._SctiesAcctAudtTrlRpt = value if value is not None else base_types.UninitialisedField(self, 'SctiesAcctAudtTrlRpt', SecuritiesAccountAuditTrailReport3, True)

	@SctiesAcctAudtTrlRpt.deleter
	def SctiesAcctAudtTrlRpt(self):
		del self._SctiesAcctAudtTrlRpt
		self._SctiesAcctAudtTrlRpt = base_types.UninitialisedField(self, 'SctiesAcctAudtTrlRpt', SecuritiesAccountAuditTrailReport3, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctiesAcctAudtTrlRpt', type=SecuritiesAccountAuditTrailReport3, min=1, max=None, mutex_group=1, array=True),
	))