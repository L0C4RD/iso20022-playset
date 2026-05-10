from . import base_types
from ._SecuritiesAccountAuditTrailQueryV01 import SecuritiesAccountAuditTrailQueryV01

class REDA_036_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesAcctAudtTrlQry"]
		@property
		def SctiesAcctAudtTrlQry(self):
			return self._SctiesAcctAudtTrlQry

		@SctiesAcctAudtTrlQry.setter
		def SctiesAcctAudtTrlQry(self, value):
			self._SctiesAcctAudtTrlQry = value if type(value) != base_types.auto else self.make_default("SctiesAcctAudtTrlQry")

		@SctiesAcctAudtTrlQry.deleter
		def SctiesAcctAudtTrlQry(self):
			del self._SctiesAcctAudtTrlQry
			self._SctiesAcctAudtTrlQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesAcctAudtTrlQry', type=SecuritiesAccountAuditTrailQueryV01, min=1, max=1, mutex_group=None, array=False),
		))

