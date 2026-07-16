# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchPaymentResponseV02

class ACMT_035_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.035.001.02"
		_docname = "acmt.035.001.02"

		__slots__ = ["_AcctSwtchPmtRspn"]
		@property
		def AcctSwtchPmtRspn(self):
			return self._AcctSwtchPmtRspn

		@AcctSwtchPmtRspn.setter
		def AcctSwtchPmtRspn(self, value):
			self._AcctSwtchPmtRspn = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchPmtRspn', AccountSwitchPaymentResponseV02, False)

		@AcctSwtchPmtRspn.deleter
		def AcctSwtchPmtRspn(self):
			del self._AcctSwtchPmtRspn
			self._AcctSwtchPmtRspn = base_types.UninitialisedField(self, 'AcctSwtchPmtRspn', AccountSwitchPaymentResponseV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchPmtRspn', type=AccountSwitchPaymentResponseV02, min=1, max=1, mutex_group=None, array=False),
		))