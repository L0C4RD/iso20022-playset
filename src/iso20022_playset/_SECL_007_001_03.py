# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyInNotificationV03 import BuyInNotificationV03

class SECL_007_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:secl.007.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_BuyInNtfctn"]
		@property
		def BuyInNtfctn(self):
			return self._BuyInNtfctn

		@BuyInNtfctn.setter
		def BuyInNtfctn(self, value):
			self._BuyInNtfctn = value if type(value) != base_types.auto else self.make_default("BuyInNtfctn")

		@BuyInNtfctn.deleter
		def BuyInNtfctn(self):
			del self._BuyInNtfctn
			self._BuyInNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInNtfctn', type=BuyInNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))