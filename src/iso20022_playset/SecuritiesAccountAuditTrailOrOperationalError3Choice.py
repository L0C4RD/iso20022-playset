import base_types
import ErrorHandling5
import SecuritiesAccountAuditTrailReport3

class SecuritiesAccountAuditTrailOrOperationalError3Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_SctiesAcctAudtTrlRpt"]
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
	def SctiesAcctAudtTrlRpt(self):
		return self._SctiesAcctAudtTrlRpt

	@SctiesAcctAudtTrlRpt.setter
	def SctiesAcctAudtTrlRpt(self, value):
		self._SctiesAcctAudtTrlRpt = value if type(value) != auto else self.make_default("SctiesAcctAudtTrlRpt")

	@SctiesAcctAudtTrlRpt.deleter
	def SctiesAcctAudtTrlRpt(self):
		del self._SctiesAcctAudtTrlRpt
		self._SctiesAcctAudtTrlRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctiesAcctAudtTrlRpt', type=SecuritiesAccountAuditTrailReport3, min=1, max=None, mutex_group=1, array=True),
	))

