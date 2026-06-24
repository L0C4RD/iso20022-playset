# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountExcludedMandateMaintenanceRequestV05 import AccountExcludedMandateMaintenanceRequestV05

class ACMT_015_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:acmt.015.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

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
			base_types.FieldEntry(name='AcctExcldMndtMntncReq', type=AccountExcludedMandateMaintenanceRequestV05, min=1, max=1, mutex_group=None, array=False),
		))