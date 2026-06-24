# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AmendmentAcceptanceV02 import AmendmentAcceptanceV02

class TSMT_005_001_02():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_AmdmntAccptnc"]
		@property
		def AmdmntAccptnc(self):
			return self._AmdmntAccptnc

		@AmdmntAccptnc.setter
		def AmdmntAccptnc(self, value):
			self._AmdmntAccptnc = value if type(value) != base_types.auto else self.make_default("AmdmntAccptnc")

		@AmdmntAccptnc.deleter
		def AmdmntAccptnc(self):
			del self._AmdmntAccptnc
			self._AmdmntAccptnc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntAccptnc', type=AmendmentAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))