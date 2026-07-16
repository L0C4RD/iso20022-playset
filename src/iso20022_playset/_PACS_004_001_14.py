# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PaymentReturnV14

class PACS_004_001_14():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:pacs.004.001.14"
		_docname = "pacs.004.001.14"

		__slots__ = ["_PmtRtr"]
		@property
		def PmtRtr(self):
			return self._PmtRtr

		@PmtRtr.setter
		def PmtRtr(self, value):
			self._PmtRtr = value if value is not None else base_types.UninitialisedField(self, 'PmtRtr', PaymentReturnV14, False)

		@PmtRtr.deleter
		def PmtRtr(self):
			del self._PmtRtr
			self._PmtRtr = base_types.UninitialisedField(self, 'PmtRtr', PaymentReturnV14, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='PmtRtr', type=PaymentReturnV14, min=1, max=1, mutex_group=None, array=False),
		))