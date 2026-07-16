# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LimitUtilisationJournalQueryV01

class CAMT_064_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.064.001.01"
		_docname = "camt.064.001.01"

		__slots__ = ["_LmtUtlstnJrnlQry"]
		@property
		def LmtUtlstnJrnlQry(self):
			return self._LmtUtlstnJrnlQry

		@LmtUtlstnJrnlQry.setter
		def LmtUtlstnJrnlQry(self, value):
			self._LmtUtlstnJrnlQry = value if value is not None else base_types.UninitialisedField(self, 'LmtUtlstnJrnlQry', LimitUtilisationJournalQueryV01, False)

		@LmtUtlstnJrnlQry.deleter
		def LmtUtlstnJrnlQry(self):
			del self._LmtUtlstnJrnlQry
			self._LmtUtlstnJrnlQry = base_types.UninitialisedField(self, 'LmtUtlstnJrnlQry', LimitUtilisationJournalQueryV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='LmtUtlstnJrnlQry', type=LimitUtilisationJournalQueryV01, min=1, max=1, mutex_group=None, array=False),
		))