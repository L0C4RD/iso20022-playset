# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import StatusExtensionRejectionNotificationV03

class TSMT_034_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.034.001.03"
		_docname = "tsmt.034.001.03"

		__slots__ = ["_StsXtnsnRjctnNtfctn"]
		@property
		def StsXtnsnRjctnNtfctn(self):
			return self._StsXtnsnRjctnNtfctn

		@StsXtnsnRjctnNtfctn.setter
		def StsXtnsnRjctnNtfctn(self, value):
			self._StsXtnsnRjctnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'StsXtnsnRjctnNtfctn', StatusExtensionRejectionNotificationV03, False)

		@StsXtnsnRjctnNtfctn.deleter
		def StsXtnsnRjctnNtfctn(self):
			del self._StsXtnsnRjctnNtfctn
			self._StsXtnsnRjctnNtfctn = base_types.UninitialisedField(self, 'StsXtnsnRjctnNtfctn', StatusExtensionRejectionNotificationV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='StsXtnsnRjctnNtfctn', type=StatusExtensionRejectionNotificationV03, min=1, max=1, mutex_group=None, array=False),
		))