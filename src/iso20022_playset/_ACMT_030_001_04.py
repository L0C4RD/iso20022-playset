# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountSwitchRequestRedirectionV04 import AccountSwitchRequestRedirectionV04

class ACMT_030_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.030.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctSwtchReqRdrctn"]
		@property
		def AcctSwtchReqRdrctn(self):
			return self._AcctSwtchReqRdrctn

		@AcctSwtchReqRdrctn.setter
		def AcctSwtchReqRdrctn(self, value):
			self._AcctSwtchReqRdrctn = value if type(value) != base_types.auto else self.make_default("AcctSwtchReqRdrctn")

		@AcctSwtchReqRdrctn.deleter
		def AcctSwtchReqRdrctn(self):
			del self._AcctSwtchReqRdrctn
			self._AcctSwtchReqRdrctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctSwtchReqRdrctn', type=AccountSwitchRequestRedirectionV04, min=1, max=1, mutex_group=None, array=False),
		))