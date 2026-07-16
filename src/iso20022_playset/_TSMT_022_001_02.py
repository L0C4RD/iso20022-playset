# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MisMatchRejectionV02

class TSMT_022_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.022.001.02"
		_docname = "tsmt.022.001.02"

		__slots__ = ["_MisMtchRjctn"]
		@property
		def MisMtchRjctn(self):
			return self._MisMtchRjctn

		@MisMtchRjctn.setter
		def MisMtchRjctn(self, value):
			self._MisMtchRjctn = value if value is not None else base_types.UninitialisedField(self, 'MisMtchRjctn', MisMatchRejectionV02, False)

		@MisMtchRjctn.deleter
		def MisMtchRjctn(self):
			del self._MisMtchRjctn
			self._MisMtchRjctn = base_types.UninitialisedField(self, 'MisMtchRjctn', MisMatchRejectionV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchRjctn', type=MisMatchRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))