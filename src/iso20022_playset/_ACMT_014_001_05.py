from . import base_types
from ._AccountReportV05 import AccountReportV05

class ACMT_014_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctRpt"]
		@property
		def AcctRpt(self):
			return self._AcctRpt

		@AcctRpt.setter
		def AcctRpt(self, value):
			self._AcctRpt = value if type(value) != base_types.auto else self.make_default("AcctRpt")

		@AcctRpt.deleter
		def AcctRpt(self):
			del self._AcctRpt
			self._AcctRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctRpt', type=AccountReportV05, min=1, max=1, mutex_group=None, array=False),
		))

