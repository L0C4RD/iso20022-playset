# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SwitchOrderV04 import SwitchOrderV04

class SETR_013_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:setr.013.001.04",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_SwtchOrdr"]
		@property
		def SwtchOrdr(self):
			return self._SwtchOrdr

		@SwtchOrdr.setter
		def SwtchOrdr(self, value):
			self._SwtchOrdr = value if type(value) != base_types.auto else self.make_default("SwtchOrdr")

		@SwtchOrdr.deleter
		def SwtchOrdr(self):
			del self._SwtchOrdr
			self._SwtchOrdr = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdr', type=SwitchOrderV04, min=1, max=1, mutex_group=None, array=False),
		))