# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountClosingAmendmentRequestV04 import AccountClosingAmendmentRequestV04

class ACMT_020_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.020.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctClsgAmdmntReq"]
		@property
		def AcctClsgAmdmntReq(self):
			return self._AcctClsgAmdmntReq

		@AcctClsgAmdmntReq.setter
		def AcctClsgAmdmntReq(self, value):
			self._AcctClsgAmdmntReq = value if type(value) != base_types.auto else self.make_default("AcctClsgAmdmntReq")

		@AcctClsgAmdmntReq.deleter
		def AcctClsgAmdmntReq(self):
			del self._AcctClsgAmdmntReq
			self._AcctClsgAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctClsgAmdmntReq', type=AccountClosingAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))