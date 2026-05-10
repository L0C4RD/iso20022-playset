import base_types
import ForeignExchangeTradeConfirmationRequestCancellationRequestV02

class FXTR_036_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_FXTradConfReqCxlReq"]
		@property
		def FXTradConfReqCxlReq(self):
			return self._FXTradConfReqCxlReq

		@FXTradConfReqCxlReq.setter
		def FXTradConfReqCxlReq(self, value):
			self._FXTradConfReqCxlReq = value if type(value) != auto else self.make_default("FXTradConfReqCxlReq")

		@FXTradConfReqCxlReq.deleter
		def FXTradConfReqCxlReq(self):
			del self._FXTradConfReqCxlReq
			self._FXTradConfReqCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfReqCxlReq', type=ForeignExchangeTradeConfirmationRequestCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

