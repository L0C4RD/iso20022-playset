# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._NetPositionV04 import NetPositionV04

class SECL_004_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:secl.004.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_NetPos"]
		@property
		def NetPos(self):
			return self._NetPos

		@NetPos.setter
		def NetPos(self, value):
			self._NetPos = value if type(value) != base_types.auto else self.make_default("NetPos")

		@NetPos.deleter
		def NetPos(self):
			del self._NetPos
			self._NetPos = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='NetPos', type=NetPositionV04, min=1, max=1, mutex_group=None, array=False),
		))