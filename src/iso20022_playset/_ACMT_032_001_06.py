# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchBalanceTransferAcknowledgementV06

class ACMT_032_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.032.001.06"
		_docname = "acmt.032.001.06"

		__slots__ = ["_AcctSwtchBalTrfAck"]
		@property
		def AcctSwtchBalTrfAck(self):
			return self._AcctSwtchBalTrfAck

		@AcctSwtchBalTrfAck.setter
		def AcctSwtchBalTrfAck(self, value):
			self._AcctSwtchBalTrfAck = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchBalTrfAck', AccountSwitchBalanceTransferAcknowledgementV06, False)

		@AcctSwtchBalTrfAck.deleter
		def AcctSwtchBalTrfAck(self):
			del self._AcctSwtchBalTrfAck
			self._AcctSwtchBalTrfAck = base_types.UninitialisedField(self, 'AcctSwtchBalTrfAck', AccountSwitchBalanceTransferAcknowledgementV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchBalTrfAck', type=AccountSwitchBalanceTransferAcknowledgementV06, min=1, max=1, mutex_group=None, array=False),
		))