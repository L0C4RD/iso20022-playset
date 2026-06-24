# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchInformationRequestV05 import AccountSwitchInformationRequestV05

class ACMT_027_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.027.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctSwtchInfReq"]
		@property
		def AcctSwtchInfReq(self):
			return self._AcctSwtchInfReq

		@AcctSwtchInfReq.setter
		def AcctSwtchInfReq(self, value):
			self._AcctSwtchInfReq = value if type(value) != base_types.auto else self.make_default("AcctSwtchInfReq")

		@AcctSwtchInfReq.deleter
		def AcctSwtchInfReq(self):
			del self._AcctSwtchInfReq
			self._AcctSwtchInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchInfReq', type=AccountSwitchInformationRequestV05, min=1, max=1, mutex_group=None, array=False),
		))