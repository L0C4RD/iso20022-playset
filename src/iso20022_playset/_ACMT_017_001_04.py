# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountMandateMaintenanceRequestV04 import AccountMandateMaintenanceRequestV04

class ACMT_017_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctMndtMntncReq"]
		@property
		def AcctMndtMntncReq(self):
			return self._AcctMndtMntncReq

		@AcctMndtMntncReq.setter
		def AcctMndtMntncReq(self, value):
			self._AcctMndtMntncReq = value if type(value) != base_types.auto else self.make_default("AcctMndtMntncReq")

		@AcctMndtMntncReq.deleter
		def AcctMndtMntncReq(self):
			del self._AcctMndtMntncReq
			self._AcctMndtMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctMndtMntncReq', type=AccountMandateMaintenanceRequestV04, min=1, max=1, mutex_group=None, array=False),
		))