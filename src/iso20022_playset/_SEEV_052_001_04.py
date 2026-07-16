# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketClaimStatusAdviceV04

class SEEV_052_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.052.001.04"
		_docname = "seev.052.001.04"

		__slots__ = ["_MktClmStsAdvc"]
		@property
		def MktClmStsAdvc(self):
			return self._MktClmStsAdvc

		@MktClmStsAdvc.setter
		def MktClmStsAdvc(self, value):
			self._MktClmStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'MktClmStsAdvc', MarketClaimStatusAdviceV04, False)

		@MktClmStsAdvc.deleter
		def MktClmStsAdvc(self):
			del self._MktClmStsAdvc
			self._MktClmStsAdvc = base_types.UninitialisedField(self, 'MktClmStsAdvc', MarketClaimStatusAdviceV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmStsAdvc', type=MarketClaimStatusAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))