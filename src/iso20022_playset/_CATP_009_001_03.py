# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMCompletionAcknowledgementV03

class CATP_009_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.009.001.03"
		_docname = "catp.009.001.03"

		__slots__ = ["_ATMCmpltnAck"]
		@property
		def ATMCmpltnAck(self):
			return self._ATMCmpltnAck

		@ATMCmpltnAck.setter
		def ATMCmpltnAck(self, value):
			self._ATMCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMCmpltnAck', ATMCompletionAcknowledgementV03, False)

		@ATMCmpltnAck.deleter
		def ATMCmpltnAck(self):
			del self._ATMCmpltnAck
			self._ATMCmpltnAck = base_types.UninitialisedField(self, 'ATMCmpltnAck', ATMCompletionAcknowledgementV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMCmpltnAck', type=ATMCompletionAcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))