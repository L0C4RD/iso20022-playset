# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._LimitUtilisationJournalReportV01 import LimitUtilisationJournalReportV01

class CAMT_065_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.065.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_LmtUtlstnJrnlRpt"]
		@property
		def LmtUtlstnJrnlRpt(self):
			return self._LmtUtlstnJrnlRpt

		@LmtUtlstnJrnlRpt.setter
		def LmtUtlstnJrnlRpt(self, value):
			self._LmtUtlstnJrnlRpt = value if type(value) != base_types.auto else self.make_default("LmtUtlstnJrnlRpt")

		@LmtUtlstnJrnlRpt.deleter
		def LmtUtlstnJrnlRpt(self):
			del self._LmtUtlstnJrnlRpt
			self._LmtUtlstnJrnlRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='LmtUtlstnJrnlRpt', type=LimitUtilisationJournalReportV01, min=1, max=1, mutex_group=None, array=False),
		))