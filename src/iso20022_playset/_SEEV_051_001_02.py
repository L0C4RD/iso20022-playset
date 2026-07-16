# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MarketClaimCancellationRequestV02

class SEEV_051_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:seev.051.001.02"
		_docname = "seev.051.001.02"

		__slots__ = ["_MktClmCxlReq"]
		@property
		def MktClmCxlReq(self):
			return self._MktClmCxlReq

		@MktClmCxlReq.setter
		def MktClmCxlReq(self, value):
			self._MktClmCxlReq = value if value is not None else base_types.UninitialisedField(self, 'MktClmCxlReq', MarketClaimCancellationRequestV02, False)

		@MktClmCxlReq.deleter
		def MktClmCxlReq(self):
			del self._MktClmCxlReq
			self._MktClmCxlReq = base_types.UninitialisedField(self, 'MktClmCxlReq', MarketClaimCancellationRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmCxlReq', type=MarketClaimCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))