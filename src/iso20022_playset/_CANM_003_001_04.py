# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._KeyExchangeInitiationV04 import KeyExchangeInitiationV04

class CANM_003_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:canm.003.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_KeyXchgInitn"]
		@property
		def KeyXchgInitn(self):
			return self._KeyXchgInitn

		@KeyXchgInitn.setter
		def KeyXchgInitn(self, value):
			self._KeyXchgInitn = value if type(value) != base_types.auto else self.make_default("KeyXchgInitn")

		@KeyXchgInitn.deleter
		def KeyXchgInitn(self):
			del self._KeyXchgInitn
			self._KeyXchgInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='KeyXchgInitn', type=KeyExchangeInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))