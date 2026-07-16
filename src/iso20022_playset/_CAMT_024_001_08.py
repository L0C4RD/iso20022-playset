# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ModifyStandingOrderV08

class CAMT_024_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.024.001.08"
		_docname = "camt.024.001.08"

		__slots__ = ["_ModfyStgOrdr"]
		@property
		def ModfyStgOrdr(self):
			return self._ModfyStgOrdr

		@ModfyStgOrdr.setter
		def ModfyStgOrdr(self, value):
			self._ModfyStgOrdr = value if value is not None else base_types.UninitialisedField(self, 'ModfyStgOrdr', ModifyStandingOrderV08, False)

		@ModfyStgOrdr.deleter
		def ModfyStgOrdr(self):
			del self._ModfyStgOrdr
			self._ModfyStgOrdr = base_types.UninitialisedField(self, 'ModfyStgOrdr', ModifyStandingOrderV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyStgOrdr', type=ModifyStandingOrderV08, min=1, max=1, mutex_group=None, array=False),
		))