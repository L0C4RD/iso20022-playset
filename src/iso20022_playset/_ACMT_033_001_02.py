# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchNotifyAccountSwitchCompleteV02 import AccountSwitchNotifyAccountSwitchCompleteV02

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
			self._AcctSwtchNtfyAcctSwtchCmplt = value if type(value) != base_types.auto else self.make_default("AcctSwtchNtfyAcctSwtchCmplt")

		@AcctSwtchNtfyAcctSwtchCmplt.deleter
		def AcctSwtchNtfyAcctSwtchCmplt(self):
			del self._AcctSwtchNtfyAcctSwtchCmplt
			self._AcctSwtchNtfyAcctSwtchCmplt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchNtfyAcctSwtchCmplt', type=AccountSwitchNotifyAccountSwitchCompleteV02, min=1, max=1, mutex_group=None, array=False),
		))