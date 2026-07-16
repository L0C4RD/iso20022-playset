# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountMandateMaintenanceRequestV04

class ACMT_017_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.017.001.04"
		_docname = "acmt.017.001.04"

		__slots__ = ["_AcctMndtMntncReq"]
		@property
		def AcctMndtMntncReq(self):
			return self._AcctMndtMntncReq

		@AcctMndtMntncReq.setter
		def AcctMndtMntncReq(self, value):
			self._AcctMndtMntncReq = value if value is not None else base_types.UninitialisedField(self, 'AcctMndtMntncReq', AccountMandateMaintenanceRequestV04, False)

		@AcctMndtMntncReq.deleter
		def AcctMndtMntncReq(self):
			del self._AcctMndtMntncReq
			self._AcctMndtMntncReq = base_types.UninitialisedField(self, 'AcctMndtMntncReq', AccountMandateMaintenanceRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctMndtMntncReq', type=AccountMandateMaintenanceRequestV04, min=1, max=1, mutex_group=None, array=False),
		))