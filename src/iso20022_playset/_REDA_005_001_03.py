# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestmentFundReportRequestV03

class REDA_005_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.005.001.03"
		_docname = "reda.005.001.03"

		__slots__ = ["_InvstmtFndRptReq"]
		@property
		def InvstmtFndRptReq(self):
			return self._InvstmtFndRptReq

		@InvstmtFndRptReq.setter
		def InvstmtFndRptReq(self, value):
			self._InvstmtFndRptReq = value if value is not None else base_types.UninitialisedField(self, 'InvstmtFndRptReq', InvestmentFundReportRequestV03, False)

		@InvstmtFndRptReq.deleter
		def InvstmtFndRptReq(self):
			del self._InvstmtFndRptReq
			self._InvstmtFndRptReq = base_types.UninitialisedField(self, 'InvstmtFndRptReq', InvestmentFundReportRequestV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvstmtFndRptReq', type=InvestmentFundReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))