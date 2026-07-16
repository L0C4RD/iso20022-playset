# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClaimNonReceiptV10

class CAMT_027_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.027.001.10"
		_docname = "camt.027.001.10"

		__slots__ = ["_ClmNonRct"]
		@property
		def ClmNonRct(self):
			return self._ClmNonRct

		@ClmNonRct.setter
		def ClmNonRct(self, value):
			self._ClmNonRct = value if value is not None else base_types.UninitialisedField(self, 'ClmNonRct', ClaimNonReceiptV10, False)

		@ClmNonRct.deleter
		def ClmNonRct(self):
			del self._ClmNonRct
			self._ClmNonRct = base_types.UninitialisedField(self, 'ClmNonRct', ClaimNonReceiptV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ClmNonRct', type=ClaimNonReceiptV10, min=1, max=1, mutex_group=None, array=False),
		))