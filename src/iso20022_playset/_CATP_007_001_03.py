# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMInquiryResponseV03

class CATP_007_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.007.001.03"
		_docname = "catp.007.001.03"

		__slots__ = ["_ATMNqryRspn"]
		@property
		def ATMNqryRspn(self):
			return self._ATMNqryRspn

		@ATMNqryRspn.setter
		def ATMNqryRspn(self, value):
			self._ATMNqryRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMNqryRspn', ATMInquiryResponseV03, False)

		@ATMNqryRspn.deleter
		def ATMNqryRspn(self):
			del self._ATMNqryRspn
			self._ATMNqryRspn = base_types.UninitialisedField(self, 'ATMNqryRspn', ATMInquiryResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMNqryRspn', type=ATMInquiryResponseV03, min=1, max=1, mutex_group=None, array=False),
		))