# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ModifyLimitV08

class CAMT_011_001_08():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.011.001.08"
		_docname = "camt.011.001.08"

		__slots__ = ["_ModfyLmt"]
		@property
		def ModfyLmt(self):
			return self._ModfyLmt

		@ModfyLmt.setter
		def ModfyLmt(self, value):
			self._ModfyLmt = value if value is not None else base_types.UninitialisedField(self, 'ModfyLmt', ModifyLimitV08, False)

		@ModfyLmt.deleter
		def ModfyLmt(self):
			del self._ModfyLmt
			self._ModfyLmt = base_types.UninitialisedField(self, 'ModfyLmt', ModifyLimitV08, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyLmt', type=ModifyLimitV08, min=1, max=1, mutex_group=None, array=False),
		))