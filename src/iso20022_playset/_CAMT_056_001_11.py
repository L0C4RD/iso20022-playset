# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FIToFIPaymentCancellationRequestV11

class CAMT_056_001_11():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.056.001.11"
		_docname = "camt.056.001.11"

		__slots__ = ["_FIToFIPmtCxlReq"]
		@property
		def FIToFIPmtCxlReq(self):
			return self._FIToFIPmtCxlReq

		@FIToFIPmtCxlReq.setter
		def FIToFIPmtCxlReq(self, value):
			self._FIToFIPmtCxlReq = value if value is not None else base_types.UninitialisedField(self, 'FIToFIPmtCxlReq', FIToFIPaymentCancellationRequestV11, False)

		@FIToFIPmtCxlReq.deleter
		def FIToFIPmtCxlReq(self):
			del self._FIToFIPmtCxlReq
			self._FIToFIPmtCxlReq = base_types.UninitialisedField(self, 'FIToFIPmtCxlReq', FIToFIPaymentCancellationRequestV11, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FIToFIPmtCxlReq', type=FIToFIPaymentCancellationRequestV11, min=1, max=1, mutex_group=None, array=False),
		))