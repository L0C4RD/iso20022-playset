import base_types
import AccountExcludedMandateMaintenanceRequestV04

class ACMT_015_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctExcldMndtMntncReq"]
		@property
		def AcctExcldMndtMntncReq(self):
			return self._AcctExcldMndtMntncReq

		@AcctExcldMndtMntncReq.setter
		def AcctExcldMndtMntncReq(self, value):
			self._AcctExcldMndtMntncReq = value if type(value) != auto else self.make_default("AcctExcldMndtMntncReq")

		@AcctExcldMndtMntncReq.deleter
		def AcctExcldMndtMntncReq(self):
			del self._AcctExcldMndtMntncReq
			self._AcctExcldMndtMntncReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctExcldMndtMntncReq', type=AccountExcludedMandateMaintenanceRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

