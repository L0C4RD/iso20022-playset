# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InquiryResponseV03

class CAIN_017_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.017.001.03"
		_docname = "cain.017.001.03"

		__slots__ = ["_NqryRspn"]
		@property
		def NqryRspn(self):
			return self._NqryRspn

		@NqryRspn.setter
		def NqryRspn(self, value):
			self._NqryRspn = value if value is not None else base_types.UninitialisedField(self, 'NqryRspn', InquiryResponseV03, False)

		@NqryRspn.deleter
		def NqryRspn(self):
			del self._NqryRspn
			self._NqryRspn = base_types.UninitialisedField(self, 'NqryRspn', InquiryResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='NqryRspn', type=InquiryResponseV03, min=1, max=1, mutex_group=None, array=False),
		))