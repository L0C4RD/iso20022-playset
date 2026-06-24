# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchInformationResponseV05 import AccountSwitchInformationResponseV05

class ACMT_028_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.028.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AcctSwtchInfRspn"]
		@property
		def AcctSwtchInfRspn(self):
			return self._AcctSwtchInfRspn

		@AcctSwtchInfRspn.setter
		def AcctSwtchInfRspn(self, value):
			self._AcctSwtchInfRspn = value if type(value) != base_types.auto else self.make_default("AcctSwtchInfRspn")

		@AcctSwtchInfRspn.deleter
		def AcctSwtchInfRspn(self):
			del self._AcctSwtchInfRspn
			self._AcctSwtchInfRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchInfRspn', type=AccountSwitchInformationResponseV05, min=1, max=1, mutex_group=None, array=False),
		))