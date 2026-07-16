# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketClaimCreationV03

class SEEV_050_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.050.001.03"
		_docname = "seev.050.001.03"

		__slots__ = ["_MktClmCre"]
		@property
		def MktClmCre(self):
			return self._MktClmCre

		@MktClmCre.setter
		def MktClmCre(self, value):
			self._MktClmCre = value if value is not None else base_types.UninitialisedField(self, 'MktClmCre', MarketClaimCreationV03, False)

		@MktClmCre.deleter
		def MktClmCre(self):
			del self._MktClmCre
			self._MktClmCre = base_types.UninitialisedField(self, 'MktClmCre', MarketClaimCreationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmCre', type=MarketClaimCreationV03, min=1, max=1, mutex_group=None, array=False),
		))