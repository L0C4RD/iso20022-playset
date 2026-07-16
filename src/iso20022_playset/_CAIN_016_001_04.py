# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InquiryVerificationInitiationV04

class CAIN_016_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.016.001.04"
		_docname = "cain.016.001.04"

		__slots__ = ["_NqryVrfctnInitn"]
		@property
		def NqryVrfctnInitn(self):
			return self._NqryVrfctnInitn

		@NqryVrfctnInitn.setter
		def NqryVrfctnInitn(self, value):
			self._NqryVrfctnInitn = value if value is not None else base_types.UninitialisedField(self, 'NqryVrfctnInitn', InquiryVerificationInitiationV04, False)

		@NqryVrfctnInitn.deleter
		def NqryVrfctnInitn(self):
			del self._NqryVrfctnInitn
			self._NqryVrfctnInitn = base_types.UninitialisedField(self, 'NqryVrfctnInitn', InquiryVerificationInitiationV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NqryVrfctnInitn', type=InquiryVerificationInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))