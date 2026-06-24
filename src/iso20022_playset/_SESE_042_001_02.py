# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._BuyInRegulatoryAdviceResponseV02 import BuyInRegulatoryAdviceResponseV02

class SESE_042_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:sese.042.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_BuyInRgltryAdvcRspn"]
		@property
		def BuyInRgltryAdvcRspn(self):
			return self._BuyInRgltryAdvcRspn

		@BuyInRgltryAdvcRspn.setter
		def BuyInRgltryAdvcRspn(self, value):
			self._BuyInRgltryAdvcRspn = value if type(value) != base_types.auto else self.make_default("BuyInRgltryAdvcRspn")

		@BuyInRgltryAdvcRspn.deleter
		def BuyInRgltryAdvcRspn(self):
			del self._BuyInRgltryAdvcRspn
			self._BuyInRgltryAdvcRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRgltryAdvcRspn', type=BuyInRegulatoryAdviceResponseV02, min=1, max=1, mutex_group=None, array=False),
		))