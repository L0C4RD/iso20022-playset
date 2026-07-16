# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeCaptureReportAcknowledgementV02

class FXTR_033_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.033.001.02"
		_docname = "fxtr.033.001.02"

		__slots__ = ["_FXTradCaptrRptAck"]
		@property
		def FXTradCaptrRptAck(self):
			return self._FXTradCaptrRptAck

		@FXTradCaptrRptAck.setter
		def FXTradCaptrRptAck(self, value):
			self._FXTradCaptrRptAck = value if value is not None else base_types.UninitialisedField(self, 'FXTradCaptrRptAck', ForeignExchangeTradeCaptureReportAcknowledgementV02, False)

		@FXTradCaptrRptAck.deleter
		def FXTradCaptrRptAck(self):
			del self._FXTradCaptrRptAck
			self._FXTradCaptrRptAck = base_types.UninitialisedField(self, 'FXTradCaptrRptAck', ForeignExchangeTradeCaptureReportAcknowledgementV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradCaptrRptAck', type=ForeignExchangeTradeCaptureReportAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))