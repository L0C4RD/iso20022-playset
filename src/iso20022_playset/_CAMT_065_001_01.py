# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitUtilisationJournalReportV01

class CAMT_065_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.065.001.01"
		_docname = "camt.065.001.01"

		__slots__ = ["_LmtUtlstnJrnlRpt"]
		@property
		def LmtUtlstnJrnlRpt(self):
			return self._LmtUtlstnJrnlRpt

		@LmtUtlstnJrnlRpt.setter
		def LmtUtlstnJrnlRpt(self, value):
			self._LmtUtlstnJrnlRpt = value if value is not None else base_types.UninitialisedField(self, 'LmtUtlstnJrnlRpt', LimitUtilisationJournalReportV01, False)

		@LmtUtlstnJrnlRpt.deleter
		def LmtUtlstnJrnlRpt(self):
			del self._LmtUtlstnJrnlRpt
			self._LmtUtlstnJrnlRpt = base_types.UninitialisedField(self, 'LmtUtlstnJrnlRpt', LimitUtilisationJournalReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='LmtUtlstnJrnlRpt', type=LimitUtilisationJournalReportV01, min=1, max=1, mutex_group=None, array=False),
		))