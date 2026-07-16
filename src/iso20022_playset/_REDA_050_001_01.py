# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountLinkMaintenanceRequestV01

class REDA_050_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.050.001.01"
		_docname = "reda.050.001.01"

		__slots__ = ["_AcctLkMntncReq"]
		@property
		def AcctLkMntncReq(self):
			return self._AcctLkMntncReq

		@AcctLkMntncReq.setter
		def AcctLkMntncReq(self, value):
			self._AcctLkMntncReq = value if value is not None else base_types.UninitialisedField(self, 'AcctLkMntncReq', AccountLinkMaintenanceRequestV01, False)

		@AcctLkMntncReq.deleter
		def AcctLkMntncReq(self):
			del self._AcctLkMntncReq
			self._AcctLkMntncReq = base_types.UninitialisedField(self, 'AcctLkMntncReq', AccountLinkMaintenanceRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkMntncReq', type=AccountLinkMaintenanceRequestV01, min=1, max=1, mutex_group=None, array=False),
		))