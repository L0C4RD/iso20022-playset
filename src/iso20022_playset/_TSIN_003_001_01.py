# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceFinancingCancellationRequestV01

class TSIN_003_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01"
		_docname = "tsin.003.001.01"

		__slots__ = ["_InvcFincgCxlReq"]
		@property
		def InvcFincgCxlReq(self):
			return self._InvcFincgCxlReq

		@InvcFincgCxlReq.setter
		def InvcFincgCxlReq(self, value):
			self._InvcFincgCxlReq = value if value is not None else base_types.UninitialisedField(self, 'InvcFincgCxlReq', InvoiceFinancingCancellationRequestV01, False)

		@InvcFincgCxlReq.deleter
		def InvcFincgCxlReq(self):
			del self._InvcFincgCxlReq
			self._InvcFincgCxlReq = base_types.UninitialisedField(self, 'InvcFincgCxlReq', InvoiceFinancingCancellationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcFincgCxlReq', type=InvoiceFinancingCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))