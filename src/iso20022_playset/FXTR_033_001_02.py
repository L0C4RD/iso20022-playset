from . import base_types
from .ForeignExchangeTradeCaptureReportAcknowledgementV02 import ForeignExchangeTradeCaptureReportAcknowledgementV02

class FXTR_033_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradCaptrRptAck"]
		@property
		def FXTradCaptrRptAck(self):
			return self._FXTradCaptrRptAck

		@FXTradCaptrRptAck.setter
		def FXTradCaptrRptAck(self, value):
			self._FXTradCaptrRptAck = value if type(value) != auto else self.make_default("FXTradCaptrRptAck")

		@FXTradCaptrRptAck.deleter
		def FXTradCaptrRptAck(self):
			del self._FXTradCaptrRptAck
			self._FXTradCaptrRptAck = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradCaptrRptAck', type=ForeignExchangeTradeCaptureReportAcknowledgementV02, min=1, max=1, mutex_group=None, array=False),
		))

