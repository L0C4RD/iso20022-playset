from . import base_types
from ._AccountSwitchBalanceTransferAcknowledgementV06 import AccountSwitchBalanceTransferAcknowledgementV06

class ACMT_032_001_06():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='AcctSwtchBalTrfAck', type=AccountSwitchBalanceTransferAcknowledgementV06, min=1, max=1, mutex_group=None, array=False),
		))

