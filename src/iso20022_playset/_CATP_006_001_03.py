# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMInquiryRequestV03 import ATMInquiryRequestV03

class CATP_006_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:catp.006.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ATMNqryReq"]
		@property
		def ATMNqryReq(self):
			return self._ATMNqryReq

		@ATMNqryReq.setter
		def ATMNqryReq(self, value):
			self._ATMNqryReq = value if type(value) != base_types.auto else self.make_default("ATMNqryReq")

		@ATMNqryReq.deleter
		def ATMNqryReq(self):
			del self._ATMNqryReq
			self._ATMNqryReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMNqryReq', type=ATMInquiryRequestV03, min=1, max=1, mutex_group=None, array=False),
		))