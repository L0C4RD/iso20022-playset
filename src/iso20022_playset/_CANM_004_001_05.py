# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._KeyExchangeResponseV05 import KeyExchangeResponseV05

class CANM_004_001_05():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:canm.004.001.05"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_KeyXchgRspn"]
		@property
		def KeyXchgRspn(self):
			return self._KeyXchgRspn

		@KeyXchgRspn.setter
		def KeyXchgRspn(self, value):
			self._KeyXchgRspn = value if type(value) != base_types.auto else self.make_default("KeyXchgRspn")

		@KeyXchgRspn.deleter
		def KeyXchgRspn(self):
			del self._KeyXchgRspn
			self._KeyXchgRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='KeyXchgRspn', type=KeyExchangeResponseV05, min=1, max=1, mutex_group=None, array=False),
		))