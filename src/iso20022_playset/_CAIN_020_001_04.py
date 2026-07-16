# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmendmentV04

class CAIN_020_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cain.020.001.04"
		_docname = "cain.020.001.04"

		__slots__ = ["_Amdmnt"]
		@property
		def Amdmnt(self):
			return self._Amdmnt

		@Amdmnt.setter
		def Amdmnt(self, value):
			self._Amdmnt = value if value is not None else base_types.UninitialisedField(self, 'Amdmnt', AmendmentV04, False)

		@Amdmnt.deleter
		def Amdmnt(self):
			del self._Amdmnt
			self._Amdmnt = base_types.UninitialisedField(self, 'Amdmnt', AmendmentV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='Amdmnt', type=AmendmentV04, min=1, max=1, mutex_group=None, array=False),
		))