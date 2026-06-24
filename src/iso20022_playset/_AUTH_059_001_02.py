# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CCPIncomeStatementAndCapitalAdequacyReportV02 import CCPIncomeStatementAndCapitalAdequacyReportV02

class AUTH_059_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:auth.059.001.02",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_CCPIncmStmtAndCptlAdqcyRpt"]
		@property
		def CCPIncmStmtAndCptlAdqcyRpt(self):
			return self._CCPIncmStmtAndCptlAdqcyRpt

		@CCPIncmStmtAndCptlAdqcyRpt.setter
		def CCPIncmStmtAndCptlAdqcyRpt(self, value):
			self._CCPIncmStmtAndCptlAdqcyRpt = value if type(value) != base_types.auto else self.make_default("CCPIncmStmtAndCptlAdqcyRpt")

		@CCPIncmStmtAndCptlAdqcyRpt.deleter
		def CCPIncmStmtAndCptlAdqcyRpt(self):
			del self._CCPIncmStmtAndCptlAdqcyRpt
			self._CCPIncmStmtAndCptlAdqcyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CCPIncmStmtAndCptlAdqcyRpt', type=CCPIncomeStatementAndCapitalAdequacyReportV02, min=1, max=1, mutex_group=None, array=False),
		))