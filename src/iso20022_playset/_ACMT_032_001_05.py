# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchBalanceTransferAcknowledgementV05 import AccountSwitchBalanceTransferAcknowledgementV05

class ACMT_032_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.032.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AcctSwtchBalTrfAck"]
		@property
		def AcctSwtchBalTrfAck(self):
			return self._AcctSwtchBalTrfAck

		@AcctSwtchBalTrfAck.setter
		def AcctSwtchBalTrfAck(self, value):
			self._AcctSwtchBalTrfAck = value if type(value) != base_types.auto else self.make_default("AcctSwtchBalTrfAck")

		@AcctSwtchBalTrfAck.deleter
		def AcctSwtchBalTrfAck(self):
			del self._AcctSwtchBalTrfAck
			self._AcctSwtchBalTrfAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchBalTrfAck', type=AccountSwitchBalanceTransferAcknowledgementV05, min=1, max=1, mutex_group=None, array=False),
		))