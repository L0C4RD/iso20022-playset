# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InquiryInitiationV03

class CAIN_016_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.016.001.03"
		_docname = "cain.016.001.03"

		__slots__ = ["_NqryInitn"]
		@property
		def NqryInitn(self):
			return self._NqryInitn

		@NqryInitn.setter
		def NqryInitn(self, value):
			self._NqryInitn = value if value is not None else base_types.UninitialisedField(self, 'NqryInitn', InquiryInitiationV03, False)

		@NqryInitn.deleter
		def NqryInitn(self):
			del self._NqryInitn
			self._NqryInitn = base_types.UninitialisedField(self, 'NqryInitn', InquiryInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NqryInitn', type=InquiryInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))