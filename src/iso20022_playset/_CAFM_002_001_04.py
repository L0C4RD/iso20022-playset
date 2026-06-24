# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FileActionResponseV04 import FileActionResponseV04

class CAFM_002_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cafm.002.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FileActnRspn"]
		@property
		def FileActnRspn(self):
			return self._FileActnRspn

		@FileActnRspn.setter
		def FileActnRspn(self, value):
			self._FileActnRspn = value if type(value) != base_types.auto else self.make_default("FileActnRspn")

		@FileActnRspn.deleter
		def FileActnRspn(self):
			del self._FileActnRspn
			self._FileActnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FileActnRspn', type=FileActionResponseV04, min=1, max=1, mutex_group=None, array=False),
		))