from . import base_types
from .SecuritiesAccountAuditTrailReportV01 import SecuritiesAccountAuditTrailReportV01

class REDA_037_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctAudtTrlRpt"]
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
			base_types.FieldEntry(name='SctiesAcctAudtTrlRpt', type=SecuritiesAccountAuditTrailReportV01, min=1, max=1, mutex_group=None, array=False),
		))

