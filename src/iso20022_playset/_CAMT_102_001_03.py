# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreateStandingOrderV03

class CAMT_102_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.102.001.03"
		_docname = "camt.102.001.03"

		__slots__ = ["_CretStgOrdr"]
		@property
		def CretStgOrdr(self):
			return self._CretStgOrdr

		@CretStgOrdr.setter
		def CretStgOrdr(self, value):
			self._CretStgOrdr = value if value is not None else base_types.UninitialisedField(self, 'CretStgOrdr', CreateStandingOrderV03, False)

		@CretStgOrdr.deleter
		def CretStgOrdr(self):
			del self._CretStgOrdr
			self._CretStgOrdr = base_types.UninitialisedField(self, 'CretStgOrdr', CreateStandingOrderV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='CretStgOrdr', type=CreateStandingOrderV03, min=1, max=1, mutex_group=None, array=False),
		))