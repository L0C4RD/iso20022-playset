# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InquiryVerificationInitiationV04 import InquiryVerificationInitiationV04

class CAIN_016_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:cain.016.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_NqryVrfctnInitn"]
		@property
		def NqryVrfctnInitn(self):
			return self._NqryVrfctnInitn

		@NqryVrfctnInitn.setter
		def NqryVrfctnInitn(self, value):
			self._NqryVrfctnInitn = value if type(value) != base_types.auto else self.make_default("NqryVrfctnInitn")

		@NqryVrfctnInitn.deleter
		def NqryVrfctnInitn(self):
			del self._NqryVrfctnInitn
			self._NqryVrfctnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NqryVrfctnInitn', type=InquiryVerificationInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))