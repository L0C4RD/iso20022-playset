# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmendmentRejectionV02

class TSMT_007_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.007.001.02"
		_docname = "tsmt.007.001.02"

		__slots__ = ["_AmdmntRjctn"]
		@property
		def AmdmntRjctn(self):
			return self._AmdmntRjctn

		@AmdmntRjctn.setter
		def AmdmntRjctn(self, value):
			self._AmdmntRjctn = value if value is not None else base_types.UninitialisedField(self, 'AmdmntRjctn', AmendmentRejectionV02, False)

		@AmdmntRjctn.deleter
		def AmdmntRjctn(self):
			del self._AmdmntRjctn
			self._AmdmntRjctn = base_types.UninitialisedField(self, 'AmdmntRjctn', AmendmentRejectionV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntRjctn', type=AmendmentRejectionV02, min=1, max=1, mutex_group=None, array=False),
		))