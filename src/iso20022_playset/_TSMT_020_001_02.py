# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MisMatchAcceptanceV02

class TSMT_020_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.020.001.02"
		_docname = "tsmt.020.001.02"

		__slots__ = ["_MisMtchAccptnc"]
		@property
		def MisMtchAccptnc(self):
			return self._MisMtchAccptnc

		@MisMtchAccptnc.setter
		def MisMtchAccptnc(self, value):
			self._MisMtchAccptnc = value if value is not None else base_types.UninitialisedField(self, 'MisMtchAccptnc', MisMatchAcceptanceV02, False)

		@MisMtchAccptnc.deleter
		def MisMtchAccptnc(self):
			del self._MisMtchAccptnc
			self._MisMtchAccptnc = base_types.UninitialisedField(self, 'MisMtchAccptnc', MisMatchAcceptanceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='MisMtchAccptnc', type=MisMatchAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))