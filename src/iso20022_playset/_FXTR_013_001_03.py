# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ForeignExchangeTradeWithdrawalNotificationV03

class FXTR_013_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.013.001.03"
		_docname = "fxtr.013.001.03"

		__slots__ = ["_FXTradWdrwlNtfctn"]
		@property
		def FXTradWdrwlNtfctn(self):
			return self._FXTradWdrwlNtfctn

		@FXTradWdrwlNtfctn.setter
		def FXTradWdrwlNtfctn(self, value):
			self._FXTradWdrwlNtfctn = value if value is not None else base_types.UninitialisedField(self, 'FXTradWdrwlNtfctn', ForeignExchangeTradeWithdrawalNotificationV03, False)

		@FXTradWdrwlNtfctn.deleter
		def FXTradWdrwlNtfctn(self):
			del self._FXTradWdrwlNtfctn
			self._FXTradWdrwlNtfctn = base_types.UninitialisedField(self, 'FXTradWdrwlNtfctn', ForeignExchangeTradeWithdrawalNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradWdrwlNtfctn', type=ForeignExchangeTradeWithdrawalNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))