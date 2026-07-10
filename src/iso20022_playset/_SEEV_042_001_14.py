# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionInstructionStatementReportV14 import CorporateActionInstructionStatementReportV14

class SEEV_042_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.042.001.14"
		_docname = "seev.042.001.14"

		__slots__ = ["_CorpActnInstrStmtRpt"]
		@property
		def CorpActnInstrStmtRpt(self):
			return self._CorpActnInstrStmtRpt

		@CorpActnInstrStmtRpt.setter
		def CorpActnInstrStmtRpt(self, value):
			self._CorpActnInstrStmtRpt = value if type(value) != base_types.auto else self.make_default("CorpActnInstrStmtRpt")

		@CorpActnInstrStmtRpt.deleter
		def CorpActnInstrStmtRpt(self):
			del self._CorpActnInstrStmtRpt
			self._CorpActnInstrStmtRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrStmtRpt', type=CorporateActionInstructionStatementReportV14, min=1, max=1, mutex_group=None, array=False),
		))