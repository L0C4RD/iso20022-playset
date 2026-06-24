# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeTradeConfirmationRequestV02 import ForeignExchangeTradeConfirmationRequestV02

class FXTR_034_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:fxtr.034.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FXTradConfReq"]
		@property
		def FXTradConfReq(self):
			return self._FXTradConfReq

		@FXTradConfReq.setter
		def FXTradConfReq(self, value):
			self._FXTradConfReq = value if type(value) != base_types.auto else self.make_default("FXTradConfReq")

		@FXTradConfReq.deleter
		def FXTradConfReq(self):
			del self._FXTradConfReq
			self._FXTradConfReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradConfReq', type=ForeignExchangeTradeConfirmationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))