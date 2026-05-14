from . import base_types
from ._AccountExcludedMandateMaintenanceAmendmentRequestV05 import AccountExcludedMandateMaintenanceAmendmentRequestV05

class ACMT_016_001_05():

	class Document(base_types._BaseFieldType):

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

