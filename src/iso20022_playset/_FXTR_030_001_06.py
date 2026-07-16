# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeBulkStatusNotificationV06

class FXTR_030_001_06():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.030.001.06"
		_docname = "fxtr.030.001.06"

		__slots__ = ["_FXTradBlkStsNtfctn"]
		@property
		def FXTradBlkStsNtfctn(self):
			return self._FXTradBlkStsNtfctn

		@FXTradBlkStsNtfctn.setter
		def FXTradBlkStsNtfctn(self, value):
			self._FXTradBlkStsNtfctn = value if value is not None else base_types.UninitialisedField(self, 'FXTradBlkStsNtfctn', ForeignExchangeTradeBulkStatusNotificationV06, False)

		@FXTradBlkStsNtfctn.deleter
		def FXTradBlkStsNtfctn(self):
			del self._FXTradBlkStsNtfctn
			self._FXTradBlkStsNtfctn = base_types.UninitialisedField(self, 'FXTradBlkStsNtfctn', ForeignExchangeTradeBulkStatusNotificationV06, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradBlkStsNtfctn', type=ForeignExchangeTradeBulkStatusNotificationV06, min=1, max=1, mutex_group=None, array=False),
		))