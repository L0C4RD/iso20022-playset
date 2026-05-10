import base_types
import AccountSwitchNotifyAccountSwitchCompleteV02

class ACMT_033_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctSwtchNtfyAcctSwtchCmplt"]
		@property
		def AcctSwtchNtfyAcctSwtchCmplt(self):
			return self._AcctSwtchNtfyAcctSwtchCmplt

		@AcctSwtchNtfyAcctSwtchCmplt.setter
		def AcctSwtchNtfyAcctSwtchCmplt(self, value):
			self._AcctSwtchNtfyAcctSwtchCmplt = value if type(value) != auto else self.make_default("AcctSwtchNtfyAcctSwtchCmplt")

		@AcctSwtchNtfyAcctSwtchCmplt.deleter
		def AcctSwtchNtfyAcctSwtchCmplt(self):
			del self._AcctSwtchNtfyAcctSwtchCmplt
			self._AcctSwtchNtfyAcctSwtchCmplt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchNtfyAcctSwtchCmplt', type=AccountSwitchNotifyAccountSwitchCompleteV02, min=1, max=1, mutex_group=None, array=False),
		))

