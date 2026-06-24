# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InformationRequestOpeningV02 import InformationRequestOpeningV02

class AUTH_001_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.001.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_InfReqOpng"]
		@property
		def InfReqOpng(self):
			return self._InfReqOpng

		@InfReqOpng.setter
		def InfReqOpng(self, value):
			self._InfReqOpng = value if type(value) != base_types.auto else self.make_default("InfReqOpng")

		@InfReqOpng.deleter
		def InfReqOpng(self):
			del self._InfReqOpng
			self._InfReqOpng = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InfReqOpng', type=InformationRequestOpeningV02, min=1, max=1, mutex_group=None, array=False),
		))