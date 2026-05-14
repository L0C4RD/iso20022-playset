# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MarketClaimCancellationRequestStatusAdviceV03 import MarketClaimCancellationRequestStatusAdviceV03

class SEEV_053_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MktClmCxlReqStsAdvc"]
		@property
		def MktClmCxlReqStsAdvc(self):
			return self._MktClmCxlReqStsAdvc

		@MktClmCxlReqStsAdvc.setter
		def MktClmCxlReqStsAdvc(self, value):
			self._MktClmCxlReqStsAdvc = value if type(value) != base_types.auto else self.make_default("MktClmCxlReqStsAdvc")

		@MktClmCxlReqStsAdvc.deleter
		def MktClmCxlReqStsAdvc(self):
			del self._MktClmCxlReqStsAdvc
			self._MktClmCxlReqStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmCxlReqStsAdvc', type=MarketClaimCancellationRequestStatusAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))