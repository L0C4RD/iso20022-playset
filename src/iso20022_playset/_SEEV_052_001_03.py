# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MarketClaimStatusAdviceV03 import MarketClaimStatusAdviceV03

class SEEV_052_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:seev.052.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

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
			base_types.FieldEntry(name='MktClmStsAdvc', type=MarketClaimStatusAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))