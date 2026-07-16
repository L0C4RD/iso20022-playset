# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmendmentAcceptanceNotificationV03

class TSMT_006_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.006.001.03"
		_docname = "tsmt.006.001.03"

		__slots__ = ["_AmdmntAccptncNtfctn"]
		@property
		def AmdmntAccptncNtfctn(self):
			return self._AmdmntAccptncNtfctn

		@AmdmntAccptncNtfctn.setter
		def AmdmntAccptncNtfctn(self, value):
			self._AmdmntAccptncNtfctn = value if value is not None else base_types.UninitialisedField(self, 'AmdmntAccptncNtfctn', AmendmentAcceptanceNotificationV03, False)

		@AmdmntAccptncNtfctn.deleter
		def AmdmntAccptncNtfctn(self):
			del self._AmdmntAccptncNtfctn
			self._AmdmntAccptncNtfctn = base_types.UninitialisedField(self, 'AmdmntAccptncNtfctn', AmendmentAcceptanceNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AmdmntAccptncNtfctn', type=AmendmentAcceptanceNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))