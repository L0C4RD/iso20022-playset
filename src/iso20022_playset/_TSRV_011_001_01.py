# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingNonExtensionNotificationV01

class TSRV_011_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.011.001.01"
		_docname = "tsrv.011.001.01"

		__slots__ = ["_UdrtkgNonXtnsnNtfctn"]
		@property
		def UdrtkgNonXtnsnNtfctn(self):
			return self._UdrtkgNonXtnsnNtfctn

		@UdrtkgNonXtnsnNtfctn.setter
		def UdrtkgNonXtnsnNtfctn(self, value):
			self._UdrtkgNonXtnsnNtfctn = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgNonXtnsnNtfctn', UndertakingNonExtensionNotificationV01, False)

		@UdrtkgNonXtnsnNtfctn.deleter
		def UdrtkgNonXtnsnNtfctn(self):
			del self._UdrtkgNonXtnsnNtfctn
			self._UdrtkgNonXtnsnNtfctn = base_types.UninitialisedField(self, 'UdrtkgNonXtnsnNtfctn', UndertakingNonExtensionNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgNonXtnsnNtfctn', type=UndertakingNonExtensionNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))