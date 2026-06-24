# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchCancelExistingPaymentV06 import AccountSwitchCancelExistingPaymentV06

class ACMT_029_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.029.001.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AcctSwtchCclExstgPmt"]
		@property
		def AcctSwtchCclExstgPmt(self):
			return self._AcctSwtchCclExstgPmt

		@AcctSwtchCclExstgPmt.setter
		def AcctSwtchCclExstgPmt(self, value):
			self._AcctSwtchCclExstgPmt = value if type(value) != base_types.auto else self.make_default("AcctSwtchCclExstgPmt")

		@AcctSwtchCclExstgPmt.deleter
		def AcctSwtchCclExstgPmt(self):
			del self._AcctSwtchCclExstgPmt
			self._AcctSwtchCclExstgPmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchCclExstgPmt', type=AccountSwitchCancelExistingPaymentV06, min=1, max=1, mutex_group=None, array=False),
		))