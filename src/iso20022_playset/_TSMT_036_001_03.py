# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusExtensionRequestNotificationV03

class TSMT_036_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.036.001.03"
		_docname = "tsmt.036.001.03"

		__slots__ = ["_StsXtnsnReqNtfctn"]
		@property
		def StsXtnsnReqNtfctn(self):
			return self._StsXtnsnReqNtfctn

		@StsXtnsnReqNtfctn.setter
		def StsXtnsnReqNtfctn(self, value):
			self._StsXtnsnReqNtfctn = value if value is not None else base_types.UninitialisedField(self, 'StsXtnsnReqNtfctn', StatusExtensionRequestNotificationV03, False)

		@StsXtnsnReqNtfctn.deleter
		def StsXtnsnReqNtfctn(self):
			del self._StsXtnsnReqNtfctn
			self._StsXtnsnReqNtfctn = base_types.UninitialisedField(self, 'StsXtnsnReqNtfctn', StatusExtensionRequestNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnReqNtfctn', type=StatusExtensionRequestNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))