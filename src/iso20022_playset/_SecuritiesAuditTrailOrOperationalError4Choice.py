from . import base_types
from .ErrorHandling5 import ErrorHandling5
from .SecuritiesAuditTrailReport4 import SecuritiesAuditTrailReport4

class SecuritiesAuditTrailOrOperationalError4Choice(base_types._BaseFieldType):

	__slots__ = ["_OprlErr", "_SctiesAudtTrlRpt"]
	@property
	def OprlErr(self):
		return self._OprlErr

	@OprlErr.setter
	def OprlErr(self, value):
		self._OprlErr = value if type(value) != base_types.auto else self.make_default("OprlErr")

	@OprlErr.deleter
	def OprlErr(self):
		del self._OprlErr
		self._OprlErr = None

	@property
	def SctiesAudtTrlRpt(self):
		return self._SctiesAudtTrlRpt

	@SctiesAudtTrlRpt.setter
	def SctiesAudtTrlRpt(self, value):
		self._SctiesAudtTrlRpt = value if type(value) != base_types.auto else self.make_default("SctiesAudtTrlRpt")

	@SctiesAudtTrlRpt.deleter
	def SctiesAudtTrlRpt(self):
		del self._SctiesAudtTrlRpt
		self._SctiesAudtTrlRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OprlErr', type=ErrorHandling5, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='SctiesAudtTrlRpt', type=SecuritiesAuditTrailReport4, min=1, max=None, mutex_group=1, array=True),
	))

