# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ModifyMemberV04

class CAMT_015_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.015.001.04"
		_docname = "camt.015.001.04"

		__slots__ = ["_ModfyMmb"]
		@property
		def ModfyMmb(self):
			return self._ModfyMmb

		@ModfyMmb.setter
		def ModfyMmb(self, value):
			self._ModfyMmb = value if value is not None else base_types.UninitialisedField(self, 'ModfyMmb', ModifyMemberV04, False)

		@ModfyMmb.deleter
		def ModfyMmb(self):
			del self._ModfyMmb
			self._ModfyMmb = base_types.UninitialisedField(self, 'ModfyMmb', ModifyMemberV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyMmb', type=ModifyMemberV04, min=1, max=1, mutex_group=None, array=False),
		))