# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeTradeStatusAndDetailsNotificationV06 import ForeignExchangeTradeStatusAndDetailsNotificationV06

class FXTR_017_001_06():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:fxtr.017.001.06"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_FXTradStsAndDtlsNtfctn"]
		@property
		def FXTradStsAndDtlsNtfctn(self):
			return self._FXTradStsAndDtlsNtfctn

		@FXTradStsAndDtlsNtfctn.setter
		def FXTradStsAndDtlsNtfctn(self, value):
			self._FXTradStsAndDtlsNtfctn = value if type(value) != base_types.auto else self.make_default("FXTradStsAndDtlsNtfctn")

		@FXTradStsAndDtlsNtfctn.deleter
		def FXTradStsAndDtlsNtfctn(self):
			del self._FXTradStsAndDtlsNtfctn
			self._FXTradStsAndDtlsNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradStsAndDtlsNtfctn', type=ForeignExchangeTradeStatusAndDetailsNotificationV06, min=1, max=1, mutex_group=None, array=False),
		))