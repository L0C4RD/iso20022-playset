# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountExcludedMandateMaintenanceAmendmentRequestV05 import AccountExcludedMandateMaintenanceAmendmentRequestV05

class ACMT_016_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.016.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AcctExcldMndtMntncAmdmntReq"]
		@property
		def AcctExcldMndtMntncAmdmntReq(self):
			return self._AcctExcldMndtMntncAmdmntReq

		@AcctExcldMndtMntncAmdmntReq.setter
		def AcctExcldMndtMntncAmdmntReq(self, value):
			self._AcctExcldMndtMntncAmdmntReq = value if type(value) != base_types.auto else self.make_default("AcctExcldMndtMntncAmdmntReq")

		@AcctExcldMndtMntncAmdmntReq.deleter
		def AcctExcldMndtMntncAmdmntReq(self):
			del self._AcctExcldMndtMntncAmdmntReq
			self._AcctExcldMndtMntncAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctExcldMndtMntncAmdmntReq', type=AccountExcludedMandateMaintenanceAmendmentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))