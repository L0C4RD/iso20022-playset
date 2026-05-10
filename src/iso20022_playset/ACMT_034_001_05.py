from . import base_types
from .AccountSwitchRequestPaymentV05 import AccountSwitchRequestPaymentV05

class ACMT_034_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchReqPmt"]
		@property
		def AcctSwtchReqPmt(self):
			return self._AcctSwtchReqPmt

		@AcctSwtchReqPmt.setter
		def AcctSwtchReqPmt(self, value):
			self._AcctSwtchReqPmt = value if type(value) != auto else self.make_default("AcctSwtchReqPmt")

		@AcctSwtchReqPmt.deleter
		def AcctSwtchReqPmt(self):
			del self._AcctSwtchReqPmt
			self._AcctSwtchReqPmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchReqPmt', type=AccountSwitchRequestPaymentV05, min=1, max=1, mutex_group=None, array=False),
		))

