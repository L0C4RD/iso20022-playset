# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvestmentFundReportRequestV03 import InvestmentFundReportRequestV03

class REDA_005_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:reda.005.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_InvstmtFndRptReq"]
		@property
		def InvstmtFndRptReq(self):
			return self._InvstmtFndRptReq

		@InvstmtFndRptReq.setter
		def InvstmtFndRptReq(self, value):
			self._InvstmtFndRptReq = value if type(value) != base_types.auto else self.make_default("InvstmtFndRptReq")

		@InvstmtFndRptReq.deleter
		def InvstmtFndRptReq(self):
			del self._InvstmtFndRptReq
			self._InvstmtFndRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvstmtFndRptReq', type=InvestmentFundReportRequestV03, min=1, max=1, mutex_group=None, array=False),
		))