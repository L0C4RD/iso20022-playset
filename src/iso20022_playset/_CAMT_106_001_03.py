# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChargesPaymentRequestV03

class CAMT_106_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.106.001.03"
		_docname = "camt.106.001.03"

		__slots__ = ["_ChrgsPmtReq"]
		@property
		def ChrgsPmtReq(self):
			return self._ChrgsPmtReq

		@ChrgsPmtReq.setter
		def ChrgsPmtReq(self, value):
			self._ChrgsPmtReq = value if value is not None else base_types.UninitialisedField(self, 'ChrgsPmtReq', ChargesPaymentRequestV03, False)

		@ChrgsPmtReq.deleter
		def ChrgsPmtReq(self):
			del self._ChrgsPmtReq
			self._ChrgsPmtReq = base_types.UninitialisedField(self, 'ChrgsPmtReq', ChargesPaymentRequestV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgsPmtReq', type=ChargesPaymentRequestV03, min=1, max=1, mutex_group=None, array=False),
		))