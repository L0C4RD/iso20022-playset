from . import base_types
import MarketClaimCreationV03

class SEEV_050_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MktClmCre"]
		@property
		def MktClmCre(self):
			return self._MktClmCre

		@MktClmCre.setter
		def MktClmCre(self, value):
			self._MktClmCre = value if type(value) != auto else self.make_default("MktClmCre")

		@MktClmCre.deleter
		def MktClmCre(self):
			del self._MktClmCre
			self._MktClmCre = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmCre', type=MarketClaimCreationV03, min=1, max=1, mutex_group=None, array=False),
		))

