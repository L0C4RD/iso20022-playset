import base_types
import ForeignExchangeTradeCaptureReportRequestV02

class FXTR_032_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradCaptrRptReq"]
		@property
		def FXTradCaptrRptReq(self):
			return self._FXTradCaptrRptReq

		@FXTradCaptrRptReq.setter
		def FXTradCaptrRptReq(self, value):
			self._FXTradCaptrRptReq = value if type(value) != auto else self.make_default("FXTradCaptrRptReq")

		@FXTradCaptrRptReq.deleter
		def FXTradCaptrRptReq(self):
			del self._FXTradCaptrRptReq
			self._FXTradCaptrRptReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradCaptrRptReq', type=ForeignExchangeTradeCaptureReportRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

