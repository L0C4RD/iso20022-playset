# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CustomerPaymentCancellationRequestV12 import CustomerPaymentCancellationRequestV12

class CAMT_055_001_12():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.055.001.12"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_CstmrPmtCxlReq"]
		@property
		def CstmrPmtCxlReq(self):
			return self._CstmrPmtCxlReq

		@CstmrPmtCxlReq.setter
		def CstmrPmtCxlReq(self, value):
			self._CstmrPmtCxlReq = value if type(value) != base_types.auto else self.make_default("CstmrPmtCxlReq")

		@CstmrPmtCxlReq.deleter
		def CstmrPmtCxlReq(self):
			del self._CstmrPmtCxlReq
			self._CstmrPmtCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='CstmrPmtCxlReq', type=CustomerPaymentCancellationRequestV12, min=1, max=1, mutex_group=None, array=False),
		))