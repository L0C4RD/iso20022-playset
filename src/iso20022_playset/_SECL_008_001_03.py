# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyInResponseV03 import BuyInResponseV03

class SECL_008_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:secl.008.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_BuyInRspn"]
		@property
		def BuyInRspn(self):
			return self._BuyInRspn

		@BuyInRspn.setter
		def BuyInRspn(self, value):
			self._BuyInRspn = value if type(value) != base_types.auto else self.make_default("BuyInRspn")

		@BuyInRspn.deleter
		def BuyInRspn(self):
			del self._BuyInRspn
			self._BuyInRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRspn', type=BuyInResponseV03, min=1, max=1, mutex_group=None, array=False),
		))