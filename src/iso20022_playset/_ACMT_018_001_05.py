# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountMandateMaintenanceAmendmentRequestV05 import AccountMandateMaintenanceAmendmentRequestV05

class ACMT_018_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.018.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AcctMndtMntncAmdmntReq"]
		@property
		def AcctMndtMntncAmdmntReq(self):
			return self._AcctMndtMntncAmdmntReq

		@AcctMndtMntncAmdmntReq.setter
		def AcctMndtMntncAmdmntReq(self, value):
			self._AcctMndtMntncAmdmntReq = value if type(value) != base_types.auto else self.make_default("AcctMndtMntncAmdmntReq")

		@AcctMndtMntncAmdmntReq.deleter
		def AcctMndtMntncAmdmntReq(self):
			del self._AcctMndtMntncAmdmntReq
			self._AcctMndtMntncAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctMndtMntncAmdmntReq', type=AccountMandateMaintenanceAmendmentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))