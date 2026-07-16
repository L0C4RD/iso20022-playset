# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeStatusAndDetailsNotificationV06

class FXTR_017_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.017.001.06"
		_docname = "fxtr.017.001.06"

		__slots__ = ["_FXTradStsAndDtlsNtfctn"]
		@property
		def FXTradStsAndDtlsNtfctn(self):
			return self._FXTradStsAndDtlsNtfctn

		@FXTradStsAndDtlsNtfctn.setter
		def FXTradStsAndDtlsNtfctn(self, value):
			self._FXTradStsAndDtlsNtfctn = value if value is not None else base_types.UninitialisedField(self, 'FXTradStsAndDtlsNtfctn', ForeignExchangeTradeStatusAndDetailsNotificationV06, False)

		@FXTradStsAndDtlsNtfctn.deleter
		def FXTradStsAndDtlsNtfctn(self):
			del self._FXTradStsAndDtlsNtfctn
			self._FXTradStsAndDtlsNtfctn = base_types.UninitialisedField(self, 'FXTradStsAndDtlsNtfctn', ForeignExchangeTradeStatusAndDetailsNotificationV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradStsAndDtlsNtfctn', type=ForeignExchangeTradeStatusAndDetailsNotificationV06, min=1, max=1, mutex_group=None, array=False),
		))