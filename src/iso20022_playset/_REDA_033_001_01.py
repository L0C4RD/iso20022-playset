from . import base_types
from .SecuritiesAuditTrailQueryV01 import SecuritiesAuditTrailQueryV01

class REDA_033_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAudtTrlQry"]
		@property
		def SctiesAudtTrlQry(self):
			return self._SctiesAudtTrlQry

		@SctiesAudtTrlQry.setter
		def SctiesAudtTrlQry(self, value):
			self._SctiesAudtTrlQry = value if type(value) != base_types.auto else self.make_default("SctiesAudtTrlQry")

		@SctiesAudtTrlQry.deleter
		def SctiesAudtTrlQry(self):
			del self._SctiesAudtTrlQry
			self._SctiesAudtTrlQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAudtTrlQry', type=SecuritiesAuditTrailQueryV01, min=1, max=1, mutex_group=None, array=False),
		))

