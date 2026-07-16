# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountClosingAdditionalInformationRequestV04

class ACMT_021_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.021.001.04"
		_docname = "acmt.021.001.04"

		__slots__ = ["_AcctClsgAddtlInfReq"]
		@property
		def AcctClsgAddtlInfReq(self):
			return self._AcctClsgAddtlInfReq

		@AcctClsgAddtlInfReq.setter
		def AcctClsgAddtlInfReq(self, value):
			self._AcctClsgAddtlInfReq = value if value is not None else base_types.UninitialisedField(self, 'AcctClsgAddtlInfReq', AccountClosingAdditionalInformationRequestV04, False)

		@AcctClsgAddtlInfReq.deleter
		def AcctClsgAddtlInfReq(self):
			del self._AcctClsgAddtlInfReq
			self._AcctClsgAddtlInfReq = base_types.UninitialisedField(self, 'AcctClsgAddtlInfReq', AccountClosingAdditionalInformationRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctClsgAddtlInfReq', type=AccountClosingAdditionalInformationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))