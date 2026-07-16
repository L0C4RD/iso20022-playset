# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyInRegulatoryAdviceV02

class SESE_041_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:sese.041.001.02"
		_docname = "sese.041.001.02"

		__slots__ = ["_BuyInRgltryAdvc"]
		@property
		def BuyInRgltryAdvc(self):
			return self._BuyInRgltryAdvc

		@BuyInRgltryAdvc.setter
		def BuyInRgltryAdvc(self, value):
			self._BuyInRgltryAdvc = value if value is not None else base_types.UninitialisedField(self, 'BuyInRgltryAdvc', BuyInRegulatoryAdviceV02, False)

		@BuyInRgltryAdvc.deleter
		def BuyInRgltryAdvc(self):
			del self._BuyInRgltryAdvc
			self._BuyInRgltryAdvc = base_types.UninitialisedField(self, 'BuyInRgltryAdvc', BuyInRegulatoryAdviceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='BuyInRgltryAdvc', type=BuyInRegulatoryAdviceV02, min=1, max=1, mutex_group=None, array=False),
		))