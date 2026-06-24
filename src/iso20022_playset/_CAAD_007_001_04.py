# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ErrorV04 import ErrorV04

class CAAD_007_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:caad.007.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_Err"]
		@property
		def Err(self):
			return self._Err

		@Err.setter
		def Err(self, value):
			self._Err = value if type(value) != base_types.auto else self.make_default("Err")

		@Err.deleter
		def Err(self):
			del self._Err
			self._Err = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Err', type=ErrorV04, min=1, max=1, mutex_group=None, array=False),
		))