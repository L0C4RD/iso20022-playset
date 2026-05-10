import base_types
import AccountOpeningAmendmentRequestV05

class ACMT_008_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctOpngAmdmntReq"]
		@property
		def AcctOpngAmdmntReq(self):
			return self._AcctOpngAmdmntReq

		@AcctOpngAmdmntReq.setter
		def AcctOpngAmdmntReq(self, value):
			self._AcctOpngAmdmntReq = value if type(value) != auto else self.make_default("AcctOpngAmdmntReq")

		@AcctOpngAmdmntReq.deleter
		def AcctOpngAmdmntReq(self):
			del self._AcctOpngAmdmntReq
			self._AcctOpngAmdmntReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngAmdmntReq', type=AccountOpeningAmendmentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))

