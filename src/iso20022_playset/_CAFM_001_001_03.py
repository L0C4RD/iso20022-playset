# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FileActionInitiationV03

class CAFM_001_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:cafm.001.001.03"
		_docname = "cafm.001.001.03"

		__slots__ = ["_FileActnInitn"]
		@property
		def FileActnInitn(self):
			return self._FileActnInitn

		@FileActnInitn.setter
		def FileActnInitn(self, value):
			self._FileActnInitn = value if value is not None else base_types.UninitialisedField(self, 'FileActnInitn', FileActionInitiationV03, False)

		@FileActnInitn.deleter
		def FileActnInitn(self):
			del self._FileActnInitn
			self._FileActnInitn = base_types.UninitialisedField(self, 'FileActnInitn', FileActionInitiationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='FileActnInitn', type=FileActionInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))