import base_types
import AccountReportRequestV04

class ACMT_013_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AcctRptReq"]
		@property
		def AcctRptReq(self):
			return self._AcctRptReq

		@AcctRptReq.setter
		def AcctRptReq(self, value):
			self._AcctRptReq = value if type(value) != auto else self.make_default("AcctRptReq")

		@AcctRptReq.deleter
		def AcctRptReq(self):
			del self._AcctRptReq
			self._AcctRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctRptReq', type=AccountReportRequestV04, min=1, max=1, mutex_group=None, array=False),
		))

