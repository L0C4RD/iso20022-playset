from . import base_types
from .AccountSwitchPaymentResponseV02 import AccountSwitchPaymentResponseV02

class ACMT_035_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchPmtRspn"]
		@property
		def AcctSwtchPmtRspn(self):
			return self._AcctSwtchPmtRspn

		@AcctSwtchPmtRspn.setter
		def AcctSwtchPmtRspn(self, value):
			self._AcctSwtchPmtRspn = value if type(value) != base_types.auto else self.make_default("AcctSwtchPmtRspn")

		@AcctSwtchPmtRspn.deleter
		def AcctSwtchPmtRspn(self):
			del self._AcctSwtchPmtRspn
			self._AcctSwtchPmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchPmtRspn', type=AccountSwitchPaymentResponseV02, min=1, max=1, mutex_group=None, array=False),
		))

