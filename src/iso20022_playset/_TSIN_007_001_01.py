# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceAssignmentStatusV01

class TSIN_007_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.007.001.01"
		_docname = "tsin.007.001.01"

		__slots__ = ["_InvcAssgnmtSts"]
		@property
		def InvcAssgnmtSts(self):
			return self._InvcAssgnmtSts

		@InvcAssgnmtSts.setter
		def InvcAssgnmtSts(self, value):
			self._InvcAssgnmtSts = value if value is not None else base_types.UninitialisedField(self, 'InvcAssgnmtSts', InvoiceAssignmentStatusV01, False)

		@InvcAssgnmtSts.deleter
		def InvcAssgnmtSts(self):
			del self._InvcAssgnmtSts
			self._InvcAssgnmtSts = base_types.UninitialisedField(self, 'InvcAssgnmtSts', InvoiceAssignmentStatusV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtSts', type=InvoiceAssignmentStatusV01, min=1, max=1, mutex_group=None, array=False),
		))