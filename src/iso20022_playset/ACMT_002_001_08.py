from . import base_types
from .AccountDetailsConfirmationV08 import AccountDetailsConfirmationV08

class ACMT_002_001_08():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctDtlsConf"]
		@property
		def AcctDtlsConf(self):
			return self._AcctDtlsConf

		@AcctDtlsConf.setter
		def AcctDtlsConf(self, value):
			self._AcctDtlsConf = value if type(value) != auto else self.make_default("AcctDtlsConf")

		@AcctDtlsConf.deleter
		def AcctDtlsConf(self):
			del self._AcctDtlsConf
			self._AcctDtlsConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctDtlsConf', type=AccountDetailsConfirmationV08, min=1, max=1, mutex_group=None, array=False),
		))

