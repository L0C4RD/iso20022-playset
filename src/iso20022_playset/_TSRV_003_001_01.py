# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UndertakingIssuanceNotificationV01

class TSRV_003_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsrv.003.001.01"
		_docname = "tsrv.003.001.01"

		__slots__ = ["_UdrtkgIssncNtfctn"]
		@property
		def UdrtkgIssncNtfctn(self):
			return self._UdrtkgIssncNtfctn

		@UdrtkgIssncNtfctn.setter
		def UdrtkgIssncNtfctn(self, value):
			self._UdrtkgIssncNtfctn = value if value is not None else base_types.UninitialisedField(self, 'UdrtkgIssncNtfctn', UndertakingIssuanceNotificationV01, False)

		@UdrtkgIssncNtfctn.deleter
		def UdrtkgIssncNtfctn(self):
			del self._UdrtkgIssncNtfctn
			self._UdrtkgIssncNtfctn = base_types.UninitialisedField(self, 'UdrtkgIssncNtfctn', UndertakingIssuanceNotificationV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='UdrtkgIssncNtfctn', type=UndertakingIssuanceNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))