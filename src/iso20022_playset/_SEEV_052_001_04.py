from . import base_types
from ._MarketClaimStatusAdviceV04 import MarketClaimStatusAdviceV04

class SEEV_052_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MktClmStsAdvc"]
		@property
		def MktClmStsAdvc(self):
			return self._MktClmStsAdvc

		@MktClmStsAdvc.setter
		def MktClmStsAdvc(self, value):
			self._MktClmStsAdvc = value if type(value) != base_types.auto else self.make_default("MktClmStsAdvc")

		@MktClmStsAdvc.deleter
		def MktClmStsAdvc(self):
			del self._MktClmStsAdvc
			self._MktClmStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmStsAdvc', type=MarketClaimStatusAdviceV04, min=1, max=1, mutex_group=None, array=False),
		))

