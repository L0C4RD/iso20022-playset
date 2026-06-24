# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LimitUtilisationJournalQueryV01 import LimitUtilisationJournalQueryV01

class CAMT_064_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.064.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_LmtUtlstnJrnlQry"]
		@property
		def LmtUtlstnJrnlQry(self):
			return self._LmtUtlstnJrnlQry

		@LmtUtlstnJrnlQry.setter
		def LmtUtlstnJrnlQry(self, value):
			self._LmtUtlstnJrnlQry = value if type(value) != base_types.auto else self.make_default("LmtUtlstnJrnlQry")

		@LmtUtlstnJrnlQry.deleter
		def LmtUtlstnJrnlQry(self):
			del self._LmtUtlstnJrnlQry
			self._LmtUtlstnJrnlQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LmtUtlstnJrnlQry', type=LimitUtilisationJournalQueryV01, min=1, max=1, mutex_group=None, array=False),
		))