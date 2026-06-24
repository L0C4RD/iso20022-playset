# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchCancelExistingPaymentV05 import AccountSwitchCancelExistingPaymentV05

class ACMT_029_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.029.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
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
			base_types.FieldEntry(name='AcctSwtchCclExstgPmt', type=AccountSwitchCancelExistingPaymentV05, min=1, max=1, mutex_group=None, array=False),
		))