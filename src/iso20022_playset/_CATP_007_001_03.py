# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMInquiryResponseV03 import ATMInquiryResponseV03

class CATP_007_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:catp.007.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ATMNqryRspn"]
		@property
		def ATMNqryRspn(self):
			return self._ATMNqryRspn

		@ATMNqryRspn.setter
		def ATMNqryRspn(self, value):
			self._ATMNqryRspn = value if type(value) != base_types.auto else self.make_default("ATMNqryRspn")

		@ATMNqryRspn.deleter
		def ATMNqryRspn(self):
			del self._ATMNqryRspn
			self._ATMNqryRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMNqryRspn', type=ATMInquiryResponseV03, min=1, max=1, mutex_group=None, array=False),
		))