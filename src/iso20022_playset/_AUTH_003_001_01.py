# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InformationRequestStatusChangeNotificationV01

class AUTH_003_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.003.001.01"
		_docname = "auth.003.001.01"

		__slots__ = ["_InfReqStsChngNtfctn"]
		@property
		def InfReqStsChngNtfctn(self):
			return self._InfReqStsChngNtfctn

		@InfReqStsChngNtfctn.setter
		def InfReqStsChngNtfctn(self, value):
			self._InfReqStsChngNtfctn = value if value is not None else base_types.UninitialisedField(self, 'InfReqStsChngNtfctn', InformationRequestStatusChangeNotificationV01, False)

		@InfReqStsChngNtfctn.deleter
		def InfReqStsChngNtfctn(self):
			del self._InfReqStsChngNtfctn
			self._InfReqStsChngNtfctn = base_types.UninitialisedField(self, 'InfReqStsChngNtfctn', InformationRequestStatusChangeNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InfReqStsChngNtfctn', type=InformationRequestStatusChangeNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))