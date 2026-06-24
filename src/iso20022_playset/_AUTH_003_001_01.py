# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InformationRequestStatusChangeNotificationV01 import InformationRequestStatusChangeNotificationV01

class AUTH_003_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types._BaseDataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:auth.003.001.01"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types._BaseDataType_String, required=True),
		))

		__slots__ = ["_InfReqStsChngNtfctn"]
		@property
		def InfReqStsChngNtfctn(self):
			return self._InfReqStsChngNtfctn

		@InfReqStsChngNtfctn.setter
		def InfReqStsChngNtfctn(self, value):
			self._InfReqStsChngNtfctn = value if type(value) != base_types.auto else self.make_default("InfReqStsChngNtfctn")

		@InfReqStsChngNtfctn.deleter
		def InfReqStsChngNtfctn(self):
			del self._InfReqStsChngNtfctn
			self._InfReqStsChngNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InfReqStsChngNtfctn', type=InformationRequestStatusChangeNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))