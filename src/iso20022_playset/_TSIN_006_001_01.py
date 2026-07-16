# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceAssignmentRequestV01

class TSIN_006_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.006.001.01"
		_docname = "tsin.006.001.01"

		__slots__ = ["_InvcAssgnmtReq"]
		@property
		def InvcAssgnmtReq(self):
			return self._InvcAssgnmtReq

		@InvcAssgnmtReq.setter
		def InvcAssgnmtReq(self, value):
			self._InvcAssgnmtReq = value if value is not None else base_types.UninitialisedField(self, 'InvcAssgnmtReq', InvoiceAssignmentRequestV01, False)

		@InvcAssgnmtReq.deleter
		def InvcAssgnmtReq(self):
			del self._InvcAssgnmtReq
			self._InvcAssgnmtReq = base_types.UninitialisedField(self, 'InvcAssgnmtReq', InvoiceAssignmentRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcAssgnmtReq', type=InvoiceAssignmentRequestV01, min=1, max=1, mutex_group=None, array=False),
		))