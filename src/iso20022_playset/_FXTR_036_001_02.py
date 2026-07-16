# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeConfirmationRequestCancellationRequestV02

class FXTR_036_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.036.001.02"
		_docname = "fxtr.036.001.02"

		__slots__ = ["_FXTradConfReqCxlReq"]
		@property
		def FXTradConfReqCxlReq(self):
			return self._FXTradConfReqCxlReq

		@FXTradConfReqCxlReq.setter
		def FXTradConfReqCxlReq(self, value):
			self._FXTradConfReqCxlReq = value if value is not None else base_types.UninitialisedField(self, 'FXTradConfReqCxlReq', ForeignExchangeTradeConfirmationRequestCancellationRequestV02, False)

		@FXTradConfReqCxlReq.deleter
		def FXTradConfReqCxlReq(self):
			del self._FXTradConfReqCxlReq
			self._FXTradConfReqCxlReq = base_types.UninitialisedField(self, 'FXTradConfReqCxlReq', ForeignExchangeTradeConfirmationRequestCancellationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfReqCxlReq', type=ForeignExchangeTradeConfirmationRequestCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))