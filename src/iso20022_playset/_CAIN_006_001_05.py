# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ReversalResponseV05 import ReversalResponseV05

class CAIN_006_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cain.006.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_RvslRspn"]
		@property
		def RvslRspn(self):
			return self._RvslRspn

		@RvslRspn.setter
		def RvslRspn(self, value):
			self._RvslRspn = value if type(value) != base_types.auto else self.make_default("RvslRspn")

		@RvslRspn.deleter
		def RvslRspn(self):
			del self._RvslRspn
			self._RvslRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslRspn', type=ReversalResponseV05, min=1, max=1, mutex_group=None, array=False),
		))