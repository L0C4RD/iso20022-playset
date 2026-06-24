# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FileActionInitiationV04 import FileActionInitiationV04

class CAFM_001_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cafm.001.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_FileActnInitn"]
		@property
		def FileActnInitn(self):
			return self._FileActnInitn

		@FileActnInitn.setter
		def FileActnInitn(self, value):
			self._FileActnInitn = value if type(value) != base_types.auto else self.make_default("FileActnInitn")

		@FileActnInitn.deleter
		def FileActnInitn(self):
			del self._FileActnInitn
			self._FileActnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='FileActnInitn', type=FileActionInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))