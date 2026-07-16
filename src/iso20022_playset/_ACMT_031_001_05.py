# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchRequestBalanceTransferV05

class ACMT_031_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.031.001.05"
		_docname = "acmt.031.001.05"

		__slots__ = ["_AcctSwtchReqBalTrf"]
		@property
		def AcctSwtchReqBalTrf(self):
			return self._AcctSwtchReqBalTrf

		@AcctSwtchReqBalTrf.setter
		def AcctSwtchReqBalTrf(self, value):
			self._AcctSwtchReqBalTrf = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchReqBalTrf', AccountSwitchRequestBalanceTransferV05, False)

		@AcctSwtchReqBalTrf.deleter
		def AcctSwtchReqBalTrf(self):
			del self._AcctSwtchReqBalTrf
			self._AcctSwtchReqBalTrf = base_types.UninitialisedField(self, 'AcctSwtchReqBalTrf', AccountSwitchRequestBalanceTransferV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchReqBalTrf', type=AccountSwitchRequestBalanceTransferV05, min=1, max=1, mutex_group=None, array=False),
		))