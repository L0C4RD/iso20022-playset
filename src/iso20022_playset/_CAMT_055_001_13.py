# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerPaymentCancellationRequestV13

class CAMT_055_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.055.001.13"
		_docname = "camt.055.001.13"

		__slots__ = ["_CstmrPmtCxlReq"]
		@property
		def CstmrPmtCxlReq(self):
			return self._CstmrPmtCxlReq

		@CstmrPmtCxlReq.setter
		def CstmrPmtCxlReq(self, value):
			self._CstmrPmtCxlReq = value if value is not None else base_types.UninitialisedField(self, 'CstmrPmtCxlReq', CustomerPaymentCancellationRequestV13, False)

		@CstmrPmtCxlReq.deleter
		def CstmrPmtCxlReq(self):
			del self._CstmrPmtCxlReq
			self._CstmrPmtCxlReq = base_types.UninitialisedField(self, 'CstmrPmtCxlReq', CustomerPaymentCancellationRequestV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtCxlReq', type=CustomerPaymentCancellationRequestV13, min=1, max=1, mutex_group=None, array=False),
		))