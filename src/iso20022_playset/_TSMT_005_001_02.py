# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmendmentAcceptanceV02

class TSMT_005_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.005.001.02"
		_docname = "tsmt.005.001.02"

		__slots__ = ["_AmdmntAccptnc"]
		@property
		def AmdmntAccptnc(self):
			return self._AmdmntAccptnc

		@AmdmntAccptnc.setter
		def AmdmntAccptnc(self, value):
			self._AmdmntAccptnc = value if value is not None else base_types.UninitialisedField(self, 'AmdmntAccptnc', AmendmentAcceptanceV02, False)

		@AmdmntAccptnc.deleter
		def AmdmntAccptnc(self):
			del self._AmdmntAccptnc
			self._AmdmntAccptnc = base_types.UninitialisedField(self, 'AmdmntAccptnc', AmendmentAcceptanceV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntAccptnc', type=AmendmentAcceptanceV02, min=1, max=1, mutex_group=None, array=False),
		))