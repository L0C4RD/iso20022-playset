# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusExtensionNotificationV03

class TSMT_032_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.032.001.03"
		_docname = "tsmt.032.001.03"

		__slots__ = ["_StsXtnsnNtfctn"]
		@property
		def StsXtnsnNtfctn(self):
			return self._StsXtnsnNtfctn

		@StsXtnsnNtfctn.setter
		def StsXtnsnNtfctn(self, value):
			self._StsXtnsnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'StsXtnsnNtfctn', StatusExtensionNotificationV03, False)

		@StsXtnsnNtfctn.deleter
		def StsXtnsnNtfctn(self):
			del self._StsXtnsnNtfctn
			self._StsXtnsnNtfctn = base_types.UninitialisedField(self, 'StsXtnsnNtfctn', StatusExtensionNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnNtfctn', type=StatusExtensionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))