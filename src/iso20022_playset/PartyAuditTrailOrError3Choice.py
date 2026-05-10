import base_types
import PartyAuditTrailReport4
import ErrorHandling5

class PartyAuditTrailOrError3Choice(base_types._BaseFieldType):

	__slots__ = ["_PtyAudtTrlRpt", "_OprlErr"]
	@property
	def PtyAudtTrlRpt(self):
		return self._PtyAudtTrlRpt

	@PtyAudtTrlRpt.setter
	def PtyAudtTrlRpt(self, value):
		self._PtyAudtTrlRpt = value if type(value) != auto else self.make_default("PtyAudtTrlRpt")

	@PtyAudtTrlRpt.deleter
	def PtyAudtTrlRpt(self):
		del self._PtyAudtTrlRpt
		self._PtyAudtTrlRpt = None

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
		base_types.FieldEntry(name='PtyAudtTrlRpt', type=PartyAuditTrailReport4, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

