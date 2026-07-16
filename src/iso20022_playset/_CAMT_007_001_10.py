# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ModifyTransactionV10

class CAMT_007_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.007.001.10"
		_docname = "camt.007.001.10"

		__slots__ = ["_ModfyTx"]
		@property
		def ModfyTx(self):
			return self._ModfyTx

		@ModfyTx.setter
		def ModfyTx(self, value):
			self._ModfyTx = value if value is not None else base_types.UninitialisedField(self, 'ModfyTx', ModifyTransactionV10, False)

		@ModfyTx.deleter
		def ModfyTx(self):
			del self._ModfyTx
			self._ModfyTx = base_types.UninitialisedField(self, 'ModfyTx', ModifyTransactionV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyTx', type=ModifyTransactionV10, min=1, max=1, mutex_group=None, array=False),
		))