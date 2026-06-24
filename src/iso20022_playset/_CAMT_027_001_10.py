# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ClaimNonReceiptV10 import ClaimNonReceiptV10

class CAMT_027_001_10():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:camt.027.001.10"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_ClmNonRct"]
		@property
		def ClmNonRct(self):
			return self._ClmNonRct

		@ClmNonRct.setter
		def ClmNonRct(self, value):
			self._ClmNonRct = value if type(value) != base_types.auto else self.make_default("ClmNonRct")

		@ClmNonRct.deleter
		def ClmNonRct(self):
			del self._ClmNonRct
			self._ClmNonRct = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ClmNonRct', type=ClaimNonReceiptV10, min=1, max=1, mutex_group=None, array=False),
		))