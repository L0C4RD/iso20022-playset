# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._TradeLegNotificationV05 import TradeLegNotificationV05

class SECL_001_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:secl.001.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_TradLegNtfctn"]
		@property
		def TradLegNtfctn(self):
			return self._TradLegNtfctn

		@TradLegNtfctn.setter
		def TradLegNtfctn(self, value):
			self._TradLegNtfctn = value if type(value) != base_types.auto else self.make_default("TradLegNtfctn")

		@TradLegNtfctn.deleter
		def TradLegNtfctn(self):
			del self._TradLegNtfctn
			self._TradLegNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='TradLegNtfctn', type=TradeLegNotificationV05, min=1, max=1, mutex_group=None, array=False),
		))