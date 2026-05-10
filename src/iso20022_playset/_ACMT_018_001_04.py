from . import base_types
from ._AccountMandateMaintenanceAmendmentRequestV04 import AccountMandateMaintenanceAmendmentRequestV04

class ACMT_018_001_04():

	class Document(base_types._BaseFieldType):

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
			base_types.FieldEntry(name='AcctMndtMntncAmdmntReq', type=AccountMandateMaintenanceAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

