from . import base_types
from .CCPIncomeStatementAndCapitalAdequacyReportV02 import CCPIncomeStatementAndCapitalAdequacyReportV02

class AUTH_059_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_CCPIncmStmtAndCptlAdqcyRpt"]
		@property
		def CCPIncmStmtAndCptlAdqcyRpt(self):
			return self._CCPIncmStmtAndCptlAdqcyRpt

		@CCPIncmStmtAndCptlAdqcyRpt.setter
		def CCPIncmStmtAndCptlAdqcyRpt(self, value):
			self._CCPIncmStmtAndCptlAdqcyRpt = value if type(value) != auto else self.make_default("CCPIncmStmtAndCptlAdqcyRpt")

		@CCPIncmStmtAndCptlAdqcyRpt.deleter
		def CCPIncmStmtAndCptlAdqcyRpt(self):
			del self._CCPIncmStmtAndCptlAdqcyRpt
			self._CCPIncmStmtAndCptlAdqcyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPIncmStmtAndCptlAdqcyRpt', type=CCPIncomeStatementAndCapitalAdequacyReportV02, min=1, max=1, mutex_group=None, array=False),
		))

