from . import base_types
from ._AccountSwitchRequestBalanceTransferV06 import AccountSwitchRequestBalanceTransferV06

class ACMT_031_001_06():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchReqBalTrf"]
		@property
		def AcctSwtchReqBalTrf(self):
			return self._AcctSwtchReqBalTrf

		@AcctSwtchReqBalTrf.setter
		def AcctSwtchReqBalTrf(self, value):
			self._AcctSwtchReqBalTrf = value if type(value) != base_types.auto else self.make_default("AcctSwtchReqBalTrf")

		@AcctSwtchReqBalTrf.deleter
		def AcctSwtchReqBalTrf(self):
			del self._AcctSwtchReqBalTrf
			self._AcctSwtchReqBalTrf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchReqBalTrf', type=AccountSwitchRequestBalanceTransferV06, min=1, max=1, mutex_group=None, array=False),
		))

