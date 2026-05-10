import base_types
import SecuritiesAuditTrailReportV01

class REDA_034_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAudtTrlRpt"]
		@property
		def SctiesAudtTrlRpt(self):
			return self._SctiesAudtTrlRpt

		@SctiesAudtTrlRpt.setter
		def SctiesAudtTrlRpt(self, value):
			self._SctiesAudtTrlRpt = value if type(value) != auto else self.make_default("SctiesAudtTrlRpt")

		@SctiesAudtTrlRpt.deleter
		def SctiesAudtTrlRpt(self):
			del self._SctiesAudtTrlRpt
			self._SctiesAudtTrlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAudtTrlRpt', type=SecuritiesAuditTrailReportV01, min=1, max=1, mutex_group=None, array=False),
		))

