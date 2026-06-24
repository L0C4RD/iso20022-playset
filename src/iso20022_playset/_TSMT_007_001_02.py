# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmendmentRejectionV02 import AmendmentRejectionV02

class TSMT_007_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AmdmntRjctn"]
		@property
		def AmdmntRjctn(self):
			return self._AmdmntRjctn

		@AmdmntRjctn.setter
		def AmdmntRjctn(self, value):
			self._AmdmntRjctn = value if type(value) != base_types.auto else self.make_default("AmdmntRjctn")

		@AmdmntRjctn.deleter
		def AmdmntRjctn(self):
			del self._AmdmntRjctn
			self._AmdmntRjctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntRjctn', type=AmendmentRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))