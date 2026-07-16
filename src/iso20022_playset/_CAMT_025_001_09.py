# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReceiptV09

class CAMT_025_001_09():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.025.001.09"
		_docname = "camt.025.001.09"

		__slots__ = ["_Rct"]
		@property
		def Rct(self):
			return self._Rct

		@Rct.setter
		def Rct(self, value):
			self._Rct = value if value is not None else base_types.UninitialisedField(self, 'Rct', ReceiptV09, False)

		@Rct.deleter
		def Rct(self):
			del self._Rct
			self._Rct = base_types.UninitialisedField(self, 'Rct', ReceiptV09, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='Rct', type=ReceiptV09, min=1, max=1, mutex_group=None, array=False),
		))