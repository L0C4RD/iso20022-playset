# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._MarginCallRequestV05 import MarginCallRequestV05

class COLR_003_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:colr.003.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_MrgnCallReq"]
		@property
		def MrgnCallReq(self):
			return self._MrgnCallReq

		@MrgnCallReq.setter
		def MrgnCallReq(self, value):
			self._MrgnCallReq = value if type(value) != base_types.auto else self.make_default("MrgnCallReq")

		@MrgnCallReq.deleter
		def MrgnCallReq(self):
			del self._MrgnCallReq
			self._MrgnCallReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='MrgnCallReq', type=MarginCallRequestV05, min=1, max=1, mutex_group=None, array=False),
		))