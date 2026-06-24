# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceFinancingRequestStatusV01 import InvoiceFinancingRequestStatusV01

class TSIN_002_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsin.002.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_InvcFincgReqSts"]
		@property
		def InvcFincgReqSts(self):
			return self._InvcFincgReqSts

		@InvcFincgReqSts.setter
		def InvcFincgReqSts(self, value):
			self._InvcFincgReqSts = value if type(value) != base_types.auto else self.make_default("InvcFincgReqSts")

		@InvcFincgReqSts.deleter
		def InvcFincgReqSts(self):
			del self._InvcFincgReqSts
			self._InvcFincgReqSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcFincgReqSts', type=InvoiceFinancingRequestStatusV01, min=1, max=1, mutex_group=None, array=False),
		))