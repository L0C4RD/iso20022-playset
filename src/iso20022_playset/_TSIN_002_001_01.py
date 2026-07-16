# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceFinancingRequestStatusV01

class TSIN_002_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01"
		_docname = "tsin.002.001.01"

		__slots__ = ["_InvcFincgReqSts"]
		@property
		def InvcFincgReqSts(self):
			return self._InvcFincgReqSts

		@InvcFincgReqSts.setter
		def InvcFincgReqSts(self, value):
			self._InvcFincgReqSts = value if value is not None else base_types.UninitialisedField(self, 'InvcFincgReqSts', InvoiceFinancingRequestStatusV01, False)

		@InvcFincgReqSts.deleter
		def InvcFincgReqSts(self):
			del self._InvcFincgReqSts
			self._InvcFincgReqSts = base_types.UninitialisedField(self, 'InvcFincgReqSts', InvoiceFinancingRequestStatusV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcFincgReqSts', type=InvoiceFinancingRequestStatusV01, min=1, max=1, mutex_group=None, array=False),
		))