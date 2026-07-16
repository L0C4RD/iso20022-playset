# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ModifyReservationV07

class CAMT_048_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.048.001.07"
		_docname = "camt.048.001.07"

		__slots__ = ["_ModfyRsvatn"]
		@property
		def ModfyRsvatn(self):
			return self._ModfyRsvatn

		@ModfyRsvatn.setter
		def ModfyRsvatn(self, value):
			self._ModfyRsvatn = value if value is not None else base_types.UninitialisedField(self, 'ModfyRsvatn', ModifyReservationV07, False)

		@ModfyRsvatn.deleter
		def ModfyRsvatn(self):
			del self._ModfyRsvatn
			self._ModfyRsvatn = base_types.UninitialisedField(self, 'ModfyRsvatn', ModifyReservationV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyRsvatn', type=ModifyReservationV07, min=1, max=1, mutex_group=None, array=False),
		))