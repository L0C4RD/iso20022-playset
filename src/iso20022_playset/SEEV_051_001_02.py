from . import base_types
from .MarketClaimCancellationRequestV02 import MarketClaimCancellationRequestV02

class SEEV_051_001_02():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MktClmCxlReq"]
		@property
		def MktClmCxlReq(self):
			return self._MktClmCxlReq

		@MktClmCxlReq.setter
		def MktClmCxlReq(self, value):
			self._MktClmCxlReq = value if type(value) != base_types.auto else self.make_default("MktClmCxlReq")

		@MktClmCxlReq.deleter
		def MktClmCxlReq(self):
			del self._MktClmCxlReq
			self._MktClmCxlReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmCxlReq', type=MarketClaimCancellationRequestV02, min=1, max=1, mutex_group=None, array=False),
		))

