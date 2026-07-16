# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountMandateMaintenanceAmendmentRequestV04

class ACMT_018_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.018.001.04"
		_docname = "acmt.018.001.04"

		__slots__ = ["_AcctMndtMntncAmdmntReq"]
		@property
		def AcctMndtMntncAmdmntReq(self):
			return self._AcctMndtMntncAmdmntReq

		@AcctMndtMntncAmdmntReq.setter
		def AcctMndtMntncAmdmntReq(self, value):
			self._AcctMndtMntncAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'AcctMndtMntncAmdmntReq', AccountMandateMaintenanceAmendmentRequestV04, False)

		@AcctMndtMntncAmdmntReq.deleter
		def AcctMndtMntncAmdmntReq(self):
			del self._AcctMndtMntncAmdmntReq
			self._AcctMndtMntncAmdmntReq = base_types.UninitialisedField(self, 'AcctMndtMntncAmdmntReq', AccountMandateMaintenanceAmendmentRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctMndtMntncAmdmntReq', type=AccountMandateMaintenanceAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))