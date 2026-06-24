# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountClosingAdditionalInformationRequestV04 import AccountClosingAdditionalInformationRequestV04

class ACMT_021_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.021.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctClsgAddtlInfReq"]
		@property
		def AcctClsgAddtlInfReq(self):
			return self._AcctClsgAddtlInfReq

		@AcctClsgAddtlInfReq.setter
		def AcctClsgAddtlInfReq(self, value):
			self._AcctClsgAddtlInfReq = value if type(value) != base_types.auto else self.make_default("AcctClsgAddtlInfReq")

		@AcctClsgAddtlInfReq.deleter
		def AcctClsgAddtlInfReq(self):
			del self._AcctClsgAddtlInfReq
			self._AcctClsgAddtlInfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctClsgAddtlInfReq', type=AccountClosingAdditionalInformationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))