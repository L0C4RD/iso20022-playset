# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyInRegulatoryAdviceResponseV02

class SESE_042_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.042.001.02"
		_docname = "sese.042.001.02"

		__slots__ = ["_BuyInRgltryAdvcRspn"]
		@property
		def BuyInRgltryAdvcRspn(self):
			return self._BuyInRgltryAdvcRspn

		@BuyInRgltryAdvcRspn.setter
		def BuyInRgltryAdvcRspn(self, value):
			self._BuyInRgltryAdvcRspn = value if value is not None else base_types.UninitialisedField(self, 'BuyInRgltryAdvcRspn', BuyInRegulatoryAdviceResponseV02, False)

		@BuyInRgltryAdvcRspn.deleter
		def BuyInRgltryAdvcRspn(self):
			del self._BuyInRgltryAdvcRspn
			self._BuyInRgltryAdvcRspn = base_types.UninitialisedField(self, 'BuyInRgltryAdvcRspn', BuyInRegulatoryAdviceResponseV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRgltryAdvcRspn', type=BuyInRegulatoryAdviceResponseV02, min=1, max=1, mutex_group=None, array=False),
		))