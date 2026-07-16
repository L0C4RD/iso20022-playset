# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ErrorV04

class CAAD_007_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.007.001.04"
		_docname = "caad.007.001.04"

		__slots__ = ["_Err"]
		@property
		def Err(self):
			return self._Err

		@Err.setter
		def Err(self, value):
			self._Err = value if value is not None else base_types.UninitialisedField(self, 'Err', ErrorV04, False)

		@Err.deleter
		def Err(self):
			del self._Err
			self._Err = base_types.UninitialisedField(self, 'Err', ErrorV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='Err', type=ErrorV04, min=1, max=1, mutex_group=None, array=False),
		))