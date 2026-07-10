# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ForeignExchangeTradeStatusNotificationV08 import ForeignExchangeTradeStatusNotificationV08

class FXTR_008_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:fxtr.008.001.08"
		_docname = "fxtr.008.001.08"

		__slots__ = ["_FXTradStsNtfctn"]
		@property
		def FXTradStsNtfctn(self):
			return self._FXTradStsNtfctn

		@FXTradStsNtfctn.setter
		def FXTradStsNtfctn(self, value):
			self._FXTradStsNtfctn = value if type(value) != base_types.auto else self.make_default("FXTradStsNtfctn")

		@FXTradStsNtfctn.deleter
		def FXTradStsNtfctn(self):
			del self._FXTradStsNtfctn
			self._FXTradStsNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FXTradStsNtfctn', type=ForeignExchangeTradeStatusNotificationV08, min=1, max=1, mutex_group=None, array=False),
		))