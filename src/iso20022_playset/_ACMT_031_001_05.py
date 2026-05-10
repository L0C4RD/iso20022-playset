from . import base_types
from ._AccountSwitchRequestBalanceTransferV05 import AccountSwitchRequestBalanceTransferV05

class ACMT_031_001_05():

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
			base_types.FieldEntry(name='AcctSwtchReqBalTrf', type=AccountSwitchRequestBalanceTransferV05, min=1, max=1, mutex_group=None, array=False),
		))

