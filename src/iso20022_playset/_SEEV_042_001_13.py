# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionInstructionStatementReportV13

class SEEV_042_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.042.001.13"
		_docname = "seev.042.001.13"

		__slots__ = ["_CorpActnInstrStmtRpt"]
		@property
		def CorpActnInstrStmtRpt(self):
			return self._CorpActnInstrStmtRpt

		@CorpActnInstrStmtRpt.setter
		def CorpActnInstrStmtRpt(self, value):
			self._CorpActnInstrStmtRpt = value if value is not None else base_types.UninitialisedField(self, 'CorpActnInstrStmtRpt', CorporateActionInstructionStatementReportV13, False)

		@CorpActnInstrStmtRpt.deleter
		def CorpActnInstrStmtRpt(self):
			del self._CorpActnInstrStmtRpt
			self._CorpActnInstrStmtRpt = base_types.UninitialisedField(self, 'CorpActnInstrStmtRpt', CorporateActionInstructionStatementReportV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CorpActnInstrStmtRpt', type=CorporateActionInstructionStatementReportV13, min=1, max=1, mutex_group=None, array=False),
		))