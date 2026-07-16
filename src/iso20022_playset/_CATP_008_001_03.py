# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCompletionAdviceV03

class CATP_008_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.008.001.03"
		_docname = "catp.008.001.03"

		__slots__ = ["_ATMCmpltnAdvc"]
		@property
		def ATMCmpltnAdvc(self):
			return self._ATMCmpltnAdvc

		@ATMCmpltnAdvc.setter
		def ATMCmpltnAdvc(self, value):
			self._ATMCmpltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMCmpltnAdvc', ATMCompletionAdviceV03, False)

		@ATMCmpltnAdvc.deleter
		def ATMCmpltnAdvc(self):
			del self._ATMCmpltnAdvc
			self._ATMCmpltnAdvc = base_types.UninitialisedField(self, 'ATMCmpltnAdvc', ATMCompletionAdviceV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMCmpltnAdvc', type=ATMCompletionAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))