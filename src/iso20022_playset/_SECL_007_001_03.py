# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyInNotificationV03

class SECL_007_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:secl.007.001.03"
		_docname = "secl.007.001.03"

		__slots__ = ["_BuyInNtfctn"]
		@property
		def BuyInNtfctn(self):
			return self._BuyInNtfctn

		@BuyInNtfctn.setter
		def BuyInNtfctn(self, value):
			self._BuyInNtfctn = value if value is not None else base_types.UninitialisedField(self, 'BuyInNtfctn', BuyInNotificationV03, False)

		@BuyInNtfctn.deleter
		def BuyInNtfctn(self):
			del self._BuyInNtfctn
			self._BuyInNtfctn = base_types.UninitialisedField(self, 'BuyInNtfctn', BuyInNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInNtfctn', type=BuyInNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))