# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import TradeLegNotificationV05

class SECL_001_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.001.001.05"
		_docname = "secl.001.001.05"

		__slots__ = ["_TradLegNtfctn"]
		@property
		def TradLegNtfctn(self):
			return self._TradLegNtfctn

		@TradLegNtfctn.setter
		def TradLegNtfctn(self, value):
			self._TradLegNtfctn = value if value is not None else base_types.UninitialisedField(self, 'TradLegNtfctn', TradeLegNotificationV05, False)

		@TradLegNtfctn.deleter
		def TradLegNtfctn(self):
			del self._TradLegNtfctn
			self._TradLegNtfctn = base_types.UninitialisedField(self, 'TradLegNtfctn', TradeLegNotificationV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradLegNtfctn', type=TradeLegNotificationV05, min=1, max=1, mutex_group=None, array=False),
		))