# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AddendumInitiationV04 import AddendumInitiationV04

class CAIN_025_001_04():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:cain.025.001.04"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_AdddmInitn"]
		@property
		def AdddmInitn(self):
			return self._AdddmInitn

		@AdddmInitn.setter
		def AdddmInitn(self, value):
			self._AdddmInitn = value if type(value) != base_types.auto else self.make_default("AdddmInitn")

		@AdddmInitn.deleter
		def AdddmInitn(self):
			del self._AdddmInitn
			self._AdddmInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AdddmInitn', type=AddendumInitiationV04, min=1, max=1, mutex_group=None, array=False),
		))