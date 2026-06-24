# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountOpeningAmendmentRequestV05 import AccountOpeningAmendmentRequestV05

class ACMT_008_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.008.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AcctOpngAmdmntReq"]
		@property
		def AcctOpngAmdmntReq(self):
			return self._AcctOpngAmdmntReq

		@AcctOpngAmdmntReq.setter
		def AcctOpngAmdmntReq(self, value):
			self._AcctOpngAmdmntReq = value if type(value) != base_types.auto else self.make_default("AcctOpngAmdmntReq")

		@AcctOpngAmdmntReq.deleter
		def AcctOpngAmdmntReq(self):
			del self._AcctOpngAmdmntReq
			self._AcctOpngAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngAmdmntReq', type=AccountOpeningAmendmentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))