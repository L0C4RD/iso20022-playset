# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeCaptureReportRequestV02

class FXTR_032_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.032.001.02"
		_docname = "fxtr.032.001.02"

		__slots__ = ["_FXTradCaptrRptReq"]
		@property
		def FXTradCaptrRptReq(self):
			return self._FXTradCaptrRptReq

		@FXTradCaptrRptReq.setter
		def FXTradCaptrRptReq(self, value):
			self._FXTradCaptrRptReq = value if value is not None else base_types.UninitialisedField(self, 'FXTradCaptrRptReq', ForeignExchangeTradeCaptureReportRequestV02, False)

		@FXTradCaptrRptReq.deleter
		def FXTradCaptrRptReq(self):
			del self._FXTradCaptrRptReq
			self._FXTradCaptrRptReq = base_types.UninitialisedField(self, 'FXTradCaptrRptReq', ForeignExchangeTradeCaptureReportRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradCaptrRptReq', type=ForeignExchangeTradeCaptureReportRequestV02, min=1, max=1, mutex_group=None, array=False),
		))