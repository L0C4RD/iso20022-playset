from . import base_types
import InvestmentFundReportRequestV03

class REDA_005_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvstmtFndRptReq"]
		@property
		def InvstmtFndRptReq(self):
			return self._InvstmtFndRptReq

		@InvstmtFndRptReq.setter
		def InvstmtFndRptReq(self, value):
			self._InvstmtFndRptReq = value if type(value) != auto else self.make_default("InvstmtFndRptReq")

		@InvstmtFndRptReq.deleter
		def InvstmtFndRptReq(self):
			del self._InvstmtFndRptReq
			self._InvstmtFndRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvstmtFndRptReq', type=InvestmentFundReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))

