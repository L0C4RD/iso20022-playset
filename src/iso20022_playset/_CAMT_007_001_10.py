# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ModifyTransactionV10 import ModifyTransactionV10

class CAMT_007_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.007.001.10"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ModfyTx"]
		@property
		def ModfyTx(self):
			return self._ModfyTx

		@ModfyTx.setter
		def ModfyTx(self, value):
			self._ModfyTx = value if type(value) != base_types.auto else self.make_default("ModfyTx")

		@ModfyTx.deleter
		def ModfyTx(self):
			del self._ModfyTx
			self._ModfyTx = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyTx', type=ModifyTransactionV10, min=1, max=1, mutex_group=None, array=False),
		))