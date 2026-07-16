# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeConfirmationRequestV02

class FXTR_034_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.02"
		_docname = "fxtr.034.001.02"

		__slots__ = ["_FXTradConfReq"]
		@property
		def FXTradConfReq(self):
			return self._FXTradConfReq

		@FXTradConfReq.setter
		def FXTradConfReq(self, value):
			self._FXTradConfReq = value if value is not None else base_types.UninitialisedField(self, 'FXTradConfReq', ForeignExchangeTradeConfirmationRequestV02, False)

		@FXTradConfReq.deleter
		def FXTradConfReq(self):
			del self._FXTradConfReq
			self._FXTradConfReq = base_types.UninitialisedField(self, 'FXTradConfReq', ForeignExchangeTradeConfirmationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfReq', type=ForeignExchangeTradeConfirmationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))