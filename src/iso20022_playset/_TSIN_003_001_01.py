# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceFinancingCancellationRequestV01 import InvoiceFinancingCancellationRequestV01

class TSIN_003_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsin.003.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_InvcFincgCxlReq"]
		@property
		def InvcFincgCxlReq(self):
			return self._InvcFincgCxlReq

		@InvcFincgCxlReq.setter
		def InvcFincgCxlReq(self, value):
			self._InvcFincgCxlReq = value if type(value) != base_types.auto else self.make_default("InvcFincgCxlReq")

		@InvcFincgCxlReq.deleter
		def InvcFincgCxlReq(self):
			del self._InvcFincgCxlReq
			self._InvcFincgCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcFincgCxlReq', type=InvoiceFinancingCancellationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))