# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountSwitchCancelExistingPaymentV06

class ACMT_029_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.029.001.06"
		_docname = "acmt.029.001.06"

		__slots__ = ["_AcctSwtchCclExstgPmt"]
		@property
		def AcctSwtchCclExstgPmt(self):
			return self._AcctSwtchCclExstgPmt

		@AcctSwtchCclExstgPmt.setter
		def AcctSwtchCclExstgPmt(self, value):
			self._AcctSwtchCclExstgPmt = value if value is not None else base_types.UninitialisedField(self, 'AcctSwtchCclExstgPmt', AccountSwitchCancelExistingPaymentV06, False)

		@AcctSwtchCclExstgPmt.deleter
		def AcctSwtchCclExstgPmt(self):
			del self._AcctSwtchCclExstgPmt
			self._AcctSwtchCclExstgPmt = base_types.UninitialisedField(self, 'AcctSwtchCclExstgPmt', AccountSwitchCancelExistingPaymentV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchCclExstgPmt', type=AccountSwitchCancelExistingPaymentV06, min=1, max=1, mutex_group=None, array=False),
		))