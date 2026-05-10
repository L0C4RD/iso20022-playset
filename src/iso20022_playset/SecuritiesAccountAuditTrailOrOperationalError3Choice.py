from . import base_types
from .SecuritiesAccountAuditTrailReport3 import SecuritiesAccountAuditTrailReport3
from .ErrorHandling5 import ErrorHandling5

class SecuritiesAccountAuditTrailOrOperationalError3Choice(base_types._BaseFieldType):

	__slots__ = ["_SctiesAcctAudtTrlRpt", "_OprlErr"]
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
		base_types.FieldEntry(name='SctiesAcctAudtTrlRpt', type=SecuritiesAccountAuditTrailReport3, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
	))

