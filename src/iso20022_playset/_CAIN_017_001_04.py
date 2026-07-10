# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InquiryVerificationResponseV04 import InquiryVerificationResponseV04

class CAIN_017_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.017.001.04"
		_docname = "cain.017.001.04"

		__slots__ = ["_NqryVrfctnRspn"]
		@property
		def NqryVrfctnRspn(self):
			return self._NqryVrfctnRspn

		@NqryVrfctnRspn.setter
		def NqryVrfctnRspn(self, value):
			self._NqryVrfctnRspn = value if type(value) != base_types.auto else self.make_default("NqryVrfctnRspn")

		@NqryVrfctnRspn.deleter
		def NqryVrfctnRspn(self):
			del self._NqryVrfctnRspn
			self._NqryVrfctnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NqryVrfctnRspn', type=InquiryVerificationResponseV04, min=1, max=1, mutex_group=None, array=False),
		))