# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountLinkMaintenanceRequestV01 import AccountLinkMaintenanceRequestV01

class REDA_050_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.050.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AcctLkMntncReq"]
		@property
		def AcctLkMntncReq(self):
			return self._AcctLkMntncReq

		@AcctLkMntncReq.setter
		def AcctLkMntncReq(self, value):
			self._AcctLkMntncReq = value if type(value) != base_types.auto else self.make_default("AcctLkMntncReq")

		@AcctLkMntncReq.deleter
		def AcctLkMntncReq(self):
			del self._AcctLkMntncReq
			self._AcctLkMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkMntncReq', type=AccountLinkMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))