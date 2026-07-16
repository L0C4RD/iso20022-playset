# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DuplicateV07

class CAMT_034_001_07():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.034.001.07"
		_docname = "camt.034.001.07"

		__slots__ = ["_Dplct"]
		@property
		def Dplct(self):
			return self._Dplct

		@Dplct.setter
		def Dplct(self, value):
			self._Dplct = value if value is not None else base_types.UninitialisedField(self, 'Dplct', DuplicateV07, False)

		@Dplct.deleter
		def Dplct(self):
			del self._Dplct
			self._Dplct = base_types.UninitialisedField(self, 'Dplct', DuplicateV07, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='Dplct', type=DuplicateV07, min=1, max=1, mutex_group=None, array=False),
		))