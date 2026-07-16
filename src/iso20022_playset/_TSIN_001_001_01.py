# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceFinancingRequestV01

class TSIN_001_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.001.001.01"
		_docname = "tsin.001.001.01"

		__slots__ = ["_InvcFincgReq"]
		@property
		def InvcFincgReq(self):
			return self._InvcFincgReq

		@InvcFincgReq.setter
		def InvcFincgReq(self, value):
			self._InvcFincgReq = value if value is not None else base_types.UninitialisedField(self, 'InvcFincgReq', InvoiceFinancingRequestV01, False)

		@InvcFincgReq.deleter
		def InvcFincgReq(self):
			del self._InvcFincgReq
			self._InvcFincgReq = base_types.UninitialisedField(self, 'InvcFincgReq', InvoiceFinancingRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcFincgReq', type=InvoiceFinancingRequestV01, min=1, max=1, mutex_group=None, array=False),
		))