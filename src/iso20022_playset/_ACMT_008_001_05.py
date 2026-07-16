# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountOpeningAmendmentRequestV05

class ACMT_008_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.008.001.05"
		_docname = "acmt.008.001.05"

		__slots__ = ["_AcctOpngAmdmntReq"]
		@property
		def AcctOpngAmdmntReq(self):
			return self._AcctOpngAmdmntReq

		@AcctOpngAmdmntReq.setter
		def AcctOpngAmdmntReq(self, value):
			self._AcctOpngAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'AcctOpngAmdmntReq', AccountOpeningAmendmentRequestV05, False)

		@AcctOpngAmdmntReq.deleter
		def AcctOpngAmdmntReq(self):
			del self._AcctOpngAmdmntReq
			self._AcctOpngAmdmntReq = base_types.UninitialisedField(self, 'AcctOpngAmdmntReq', AccountOpeningAmendmentRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngAmdmntReq', type=AccountOpeningAmendmentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))