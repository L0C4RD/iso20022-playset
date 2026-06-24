# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountExcludedMandateMaintenanceAmendmentRequestV04 import AccountExcludedMandateMaintenanceAmendmentRequestV04

class ACMT_016_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:acmt.016.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
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
			base_types.FieldEntry(name='AcctExcldMndtMntncAmdmntReq', type=AccountExcludedMandateMaintenanceAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))