# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositCompletionAcknowledgementV02

class CATP_015_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.015.001.02"
		_docname = "catp.015.001.02"

		__slots__ = ["_ATMDpstCmpltnAck"]
		@property
		def ATMDpstCmpltnAck(self):
			return self._ATMDpstCmpltnAck

		@ATMDpstCmpltnAck.setter
		def ATMDpstCmpltnAck(self, value):
			self._ATMDpstCmpltnAck = value if value is not None else base_types.UninitialisedField(self, 'ATMDpstCmpltnAck', ATMDepositCompletionAcknowledgementV02, False)

		@ATMDpstCmpltnAck.deleter
		def ATMDpstCmpltnAck(self):
			del self._ATMDpstCmpltnAck
			self._ATMDpstCmpltnAck = base_types.UninitialisedField(self, 'ATMDpstCmpltnAck', ATMDepositCompletionAcknowledgementV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstCmpltnAck', type=ATMDepositCompletionAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))