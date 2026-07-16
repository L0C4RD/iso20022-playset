# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMWithdrawalCompletionAcknowledgementV03

class CATP_004_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.004.001.03"
		_docname = "catp.004.001.03"

		__slots__ = ["_ATMWdrwlCmpltnAck"]
		@property
		def ATMWdrwlCmpltnAck(self):
			return self._ATMWdrwlCmpltnAck

		@ATMWdrwlCmpltnAck.setter
		def ATMWdrwlCmpltnAck(self, value):
			self._ATMWdrwlCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAck', ATMWithdrawalCompletionAcknowledgementV03, False)

		@ATMWdrwlCmpltnAck.deleter
		def ATMWdrwlCmpltnAck(self):
			del self._ATMWdrwlCmpltnAck
			self._ATMWdrwlCmpltnAck = base_types.UninitialisedField(self, 'ATMWdrwlCmpltnAck', ATMWithdrawalCompletionAcknowledgementV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMWdrwlCmpltnAck', type=ATMWithdrawalCompletionAcknowledgementV03, min=1, max=1, mutex_group=None, array=False),
		))