# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountExcludedMandateMaintenanceAmendmentRequestV05

class ACMT_016_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.016.001.05"
		_docname = "acmt.016.001.05"

		__slots__ = ["_AcctExcldMndtMntncAmdmntReq"]
		@property
		def AcctExcldMndtMntncAmdmntReq(self):
			return self._AcctExcldMndtMntncAmdmntReq

		@AcctExcldMndtMntncAmdmntReq.setter
		def AcctExcldMndtMntncAmdmntReq(self, value):
			self._AcctExcldMndtMntncAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'AcctExcldMndtMntncAmdmntReq', AccountExcludedMandateMaintenanceAmendmentRequestV05, False)

		@AcctExcldMndtMntncAmdmntReq.deleter
		def AcctExcldMndtMntncAmdmntReq(self):
			del self._AcctExcldMndtMntncAmdmntReq
			self._AcctExcldMndtMntncAmdmntReq = base_types.UninitialisedField(self, 'AcctExcldMndtMntncAmdmntReq', AccountExcludedMandateMaintenanceAmendmentRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctExcldMndtMntncAmdmntReq', type=AccountExcludedMandateMaintenanceAmendmentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))