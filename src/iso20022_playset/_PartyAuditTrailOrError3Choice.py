# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorHandling5
from . import PartyAuditTrailReport4

class PartyAuditTrailOrError3Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_PtyAudtTrlRpt"]
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
	def PtyAudtTrlRpt(self):
		return self._PtyAudtTrlRpt

	@PtyAudtTrlRpt.setter
	def PtyAudtTrlRpt(self, value):
		self._PtyAudtTrlRpt = value if value is not None else base_types.UninitialisedField(self, 'PtyAudtTrlRpt', PartyAuditTrailReport4, True)

	@PtyAudtTrlRpt.deleter
	def PtyAudtTrlRpt(self):
		del self._PtyAudtTrlRpt
		self._PtyAudtTrlRpt = base_types.UninitialisedField(self, 'PtyAudtTrlRpt', PartyAuditTrailReport4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='PtyAudtTrlRpt', type=PartyAuditTrailReport4, min=1, max=None, mutex_group=1, array=True),
	))