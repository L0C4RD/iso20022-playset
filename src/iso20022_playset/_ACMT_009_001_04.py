# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountOpeningAdditionalInformationRequestV04

class ACMT_009_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.009.001.04"
		_docname = "acmt.009.001.04"

		__slots__ = ["_AcctOpngAddtlInfReq"]
		@property
		def AcctOpngAddtlInfReq(self):
			return self._AcctOpngAddtlInfReq

		@AcctOpngAddtlInfReq.setter
		def AcctOpngAddtlInfReq(self, value):
			self._AcctOpngAddtlInfReq = value if value is not None else base_types.UninitialisedField(self, 'AcctOpngAddtlInfReq', AccountOpeningAdditionalInformationRequestV04, False)

		@AcctOpngAddtlInfReq.deleter
		def AcctOpngAddtlInfReq(self):
			del self._AcctOpngAddtlInfReq
			self._AcctOpngAddtlInfReq = base_types.UninitialisedField(self, 'AcctOpngAddtlInfReq', AccountOpeningAdditionalInformationRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngAddtlInfReq', type=AccountOpeningAdditionalInformationRequestV04, min=1, max=1, mutex_group=None, array=False),
		))