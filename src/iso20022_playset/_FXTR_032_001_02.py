# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeTradeCaptureReportRequestV02 import ForeignExchangeTradeCaptureReportRequestV02

class FXTR_032_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FXTradCaptrRptReq"]
		@property
		def FXTradCaptrRptReq(self):
			return self._FXTradCaptrRptReq

		@FXTradCaptrRptReq.setter
		def FXTradCaptrRptReq(self, value):
			self._FXTradCaptrRptReq = value if type(value) != base_types.auto else self.make_default("FXTradCaptrRptReq")

		@FXTradCaptrRptReq.deleter
		def FXTradCaptrRptReq(self):
			del self._FXTradCaptrRptReq
			self._FXTradCaptrRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradCaptrRptReq', type=ForeignExchangeTradeCaptureReportRequestV02, min=1, max=1, mutex_group=None, array=False),
		))