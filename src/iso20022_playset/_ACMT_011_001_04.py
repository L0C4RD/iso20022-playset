# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountRequestRejectionV04 import AccountRequestRejectionV04

class ACMT_011_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.011.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AcctReqRjctn"]
		@property
		def AcctReqRjctn(self):
			return self._AcctReqRjctn

		@AcctReqRjctn.setter
		def AcctReqRjctn(self, value):
			self._AcctReqRjctn = value if type(value) != base_types.auto else self.make_default("AcctReqRjctn")

		@AcctReqRjctn.deleter
		def AcctReqRjctn(self):
			del self._AcctReqRjctn
			self._AcctReqRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctReqRjctn', type=AccountRequestRejectionV04, min=1, max=1, mutex_group=None, array=False),
		))