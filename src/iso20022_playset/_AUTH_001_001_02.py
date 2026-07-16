# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InformationRequestOpeningV02

class AUTH_001_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.001.001.02"
		_docname = "auth.001.001.02"

		__slots__ = ["_InfReqOpng"]
		@property
		def InfReqOpng(self):
			return self._InfReqOpng

		@InfReqOpng.setter
		def InfReqOpng(self, value):
			self._InfReqOpng = value if value is not None else base_types.UninitialisedField(self, 'InfReqOpng', InformationRequestOpeningV02, False)

		@InfReqOpng.deleter
		def InfReqOpng(self):
			del self._InfReqOpng
			self._InfReqOpng = base_types.UninitialisedField(self, 'InfReqOpng', InformationRequestOpeningV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InfReqOpng', type=InformationRequestOpeningV02, min=1, max=1, mutex_group=None, array=False),
		))