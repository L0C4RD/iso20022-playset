# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InformationRequestResponseV02

class AUTH_002_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.002.001.02"
		_docname = "auth.002.001.02"

		__slots__ = ["_InfReqRspn"]
		@property
		def InfReqRspn(self):
			return self._InfReqRspn

		@InfReqRspn.setter
		def InfReqRspn(self, value):
			self._InfReqRspn = value if value is not None else base_types.UninitialisedField(self, 'InfReqRspn', InformationRequestResponseV02, False)

		@InfReqRspn.deleter
		def InfReqRspn(self):
			del self._InfReqRspn
			self._InfReqRspn = base_types.UninitialisedField(self, 'InfReqRspn', InformationRequestResponseV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InfReqRspn', type=InformationRequestResponseV02, min=1, max=1, mutex_group=None, array=False),
		))