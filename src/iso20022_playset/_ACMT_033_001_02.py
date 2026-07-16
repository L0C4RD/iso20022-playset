# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchNotifyAccountSwitchCompleteV02

class ACMT_033_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.033.001.02"
		_docname = "acmt.033.001.02"

		__slots__ = ["_AcctSwtchNtfyAcctSwtchCmplt"]
		@property
		def AcctSwtchNtfyAcctSwtchCmplt(self):
			return self._AcctSwtchNtfyAcctSwtchCmplt

		@AcctSwtchNtfyAcctSwtchCmplt.setter
		def AcctSwtchNtfyAcctSwtchCmplt(self, value):
			self._AcctSwtchNtfyAcctSwtchCmplt = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchNtfyAcctSwtchCmplt', AccountSwitchNotifyAccountSwitchCompleteV02, False)

		@AcctSwtchNtfyAcctSwtchCmplt.deleter
		def AcctSwtchNtfyAcctSwtchCmplt(self):
			del self._AcctSwtchNtfyAcctSwtchCmplt
			self._AcctSwtchNtfyAcctSwtchCmplt = base_types.UninitialisedField(self, 'AcctSwtchNtfyAcctSwtchCmplt', AccountSwitchNotifyAccountSwitchCompleteV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchNtfyAcctSwtchCmplt', type=AccountSwitchNotifyAccountSwitchCompleteV02, min=1, max=1, mutex_group=None, array=False),
		))