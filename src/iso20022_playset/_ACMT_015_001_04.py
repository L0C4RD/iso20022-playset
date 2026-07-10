# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountExcludedMandateMaintenanceRequestV04 import AccountExcludedMandateMaintenanceRequestV04

class ACMT_015_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.015.001.04"
		_docname = "acmt.015.001.04"

		__slots__ = ["_AcctExcldMndtMntncReq"]
		@property
		def AcctExcldMndtMntncReq(self):
			return self._AcctExcldMndtMntncReq

		@AcctExcldMndtMntncReq.setter
		def AcctExcldMndtMntncReq(self, value):
			self._AcctExcldMndtMntncReq = value if type(value) != base_types.auto else self.make_default("AcctExcldMndtMntncReq")

		@AcctExcldMndtMntncReq.deleter
		def AcctExcldMndtMntncReq(self):
			del self._AcctExcldMndtMntncReq
			self._AcctExcldMndtMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctExcldMndtMntncReq', type=AccountExcludedMandateMaintenanceRequestV04, min=1, max=1, mutex_group=None, array=False),
		))