# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._SaleToPOIMessageRejectionV02 import SaleToPOIMessageRejectionV02

class CASP_013_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:casp.013.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_SaleToPOIMsgRjctn"]
		@property
		def SaleToPOIMsgRjctn(self):
			return self._SaleToPOIMsgRjctn

		@SaleToPOIMsgRjctn.setter
		def SaleToPOIMsgRjctn(self, value):
			self._SaleToPOIMsgRjctn = value if type(value) != base_types.auto else self.make_default("SaleToPOIMsgRjctn")

		@SaleToPOIMsgRjctn.deleter
		def SaleToPOIMsgRjctn(self):
			del self._SaleToPOIMsgRjctn
			self._SaleToPOIMsgRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SaleToPOIMsgRjctn', type=SaleToPOIMessageRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))