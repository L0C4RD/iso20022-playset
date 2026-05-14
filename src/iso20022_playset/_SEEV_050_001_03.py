# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MarketClaimCreationV03 import MarketClaimCreationV03

class SEEV_050_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_MktClmCre"]
		@property
		def MktClmCre(self):
			return self._MktClmCre

		@MktClmCre.setter
		def MktClmCre(self, value):
			self._MktClmCre = value if type(value) != base_types.auto else self.make_default("MktClmCre")

		@MktClmCre.deleter
		def MktClmCre(self):
			del self._MktClmCre
			self._MktClmCre = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MktClmCre', type=MarketClaimCreationV03, min=1, max=1, mutex_group=None, array=False),
		))