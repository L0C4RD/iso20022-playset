from . import base_types
from .AccountSwitchRequestRedirectionV04 import AccountSwitchRequestRedirectionV04

class ACMT_030_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchReqRdrctn"]
		@property
		def AcctSwtchReqRdrctn(self):
			return self._AcctSwtchReqRdrctn

		@AcctSwtchReqRdrctn.setter
		def AcctSwtchReqRdrctn(self, value):
			self._AcctSwtchReqRdrctn = value if type(value) != base_types.auto else self.make_default("AcctSwtchReqRdrctn")

		@AcctSwtchReqRdrctn.deleter
		def AcctSwtchReqRdrctn(self):
			del self._AcctSwtchReqRdrctn
			self._AcctSwtchReqRdrctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchReqRdrctn', type=AccountSwitchRequestRedirectionV04, min=1, max=1, mutex_group=None, array=False),
		))

